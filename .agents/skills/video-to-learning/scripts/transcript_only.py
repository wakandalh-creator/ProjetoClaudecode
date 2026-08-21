#!/usr/bin/env python3
"""Get a timestamped transcript for any video/audio source, no frames.

Reuses the `watch` plugin (claude-video)'s download.py / transcribe.py /
whisper.py — same yt-dlp + Groq/OpenAI Whisper pipeline, same
~/.config/watch/.env key — but skips frames.py entirely. video-to-learning
only needs text for distillation, so this avoids burning image tokens and
avoids ffmpeg's video-filter step failing on audio-only sources (podcasts
with no video stream).

Usage: python transcript_only.py <url-or-path> [--out-dir DIR]
Prints one JSON object to stdout.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path


def _find_watch_scripts_dir() -> Path:
    patterns = [
        os.path.expanduser("~/.claude/plugins/cache/*/watch/*/scripts/watch.py"),
        os.path.expanduser("~/.claude/plugins/cache/watch/*/scripts/watch.py"),
    ]
    candidates: list[str] = []
    for pattern in patterns:
        candidates.extend(glob.glob(pattern))
    if not candidates:
        raise SystemExit(
            "Could not find the 'watch' plugin (claude-video) scripts directory. "
            "Install it first (it provides the yt-dlp + Whisper pipeline this skill reuses), "
            "e.g. run `/watch` once so the plugin is set up, then retry."
        )
    newest = max(candidates, key=os.path.getmtime)
    return Path(newest).resolve().parent


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", help="Video/audio URL or local file path")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    scripts_dir = _find_watch_scripts_dir()
    sys.path.insert(0, str(scripts_dir))
    from download import download, is_url  # noqa: E402
    from transcribe import format_transcript, parse_vtt  # noqa: E402
    from whisper import load_api_key, transcribe_video  # noqa: E402
    from frames import get_metadata  # noqa: E402  (metadata probe only, no frame extraction)

    work = Path(args.out_dir) if args.out_dir else Path(tempfile.mkdtemp(prefix="video-to-learning-"))
    work.mkdir(parents=True, exist_ok=True)

    dl = download(args.source, work / "download")
    video_path = Path(dl["video_path"])
    info = dl.get("info") or {}

    if dl.get("downloaded"):
        canonical = info.get("url") or args.source
        source_hash = "sha256:" + hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    else:
        source_hash = "sha256:" + _sha256_file(video_path)

    chapters = []
    info_json = work / "download" / "video.info.json"
    if info_json.exists():
        try:
            raw = json.loads(info_json.read_text(encoding="utf-8"))
            chapters = raw.get("chapters") or []
        except Exception:
            pass

    transcript_source = None
    transcript_text = ""
    if dl.get("subtitle_path"):
        segments = parse_vtt(dl["subtitle_path"])
        transcript_text = format_transcript(segments)
        transcript_source = "captions"
    else:
        backend, api_key = load_api_key(None)
        if backend and api_key:
            segments, used_backend = transcribe_video(
                str(video_path), work / "audio.mp3", backend=backend, api_key=api_key,
            )
            transcript_text = format_transcript(segments)
            transcript_source = f"whisper ({used_backend})"
        else:
            transcript_source = None

    try:
        duration = get_metadata(str(video_path)).get("duration_seconds", 0)
    except SystemExit:
        duration = 0

    print(json.dumps({
        "source": args.source,
        "is_url": is_url(args.source),
        "title": info.get("title"),
        "uploader": info.get("uploader"),
        "canonical_url": info.get("url"),
        "duration_seconds": duration,
        "source_hash": source_hash,
        "chapters": [{"title": c.get("title"), "start": c.get("start_time")} for c in chapters],
        "transcript_source": transcript_source,
        "transcript": transcript_text,
        "work_dir": str(work),
    }, indent=2, ensure_ascii=False))

    if not transcript_text:
        print(
            "[video-to-learning] no captions and no Whisper key configured — "
            "run `python3 " + str(scripts_dir / "setup.py") + "` to enable transcription, "
            "or set GROQ_API_KEY/OPENAI_API_KEY in ~/.config/watch/.env",
            file=sys.stderr,
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

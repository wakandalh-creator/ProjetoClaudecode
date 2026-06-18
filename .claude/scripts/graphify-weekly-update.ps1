# Headless graphify rebuild for ProjetoClaudecode.
# Runs unattended (Windows Task Scheduler) - no Claude Code session needed.
# Requires GOOGLE_API_KEY (or GEMINI_API_KEY) set as a persistent User/Machine
# environment variable - semantic extraction and community labeling both use it.

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$ProjectRoot = "C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode"
$VaultDir    = "C:\Users\lucas\OneDrive\Área de Trabalho\Cerebro Claude\Codigo"
$ScopePaths  = @("monitor", "config", "reports", "CLAUDE.md")
$LogFile     = Join-Path $ProjectRoot ".claude\scripts\graphify-weekly-update.log"

Set-Location $ProjectRoot

if (-not ($env:GOOGLE_API_KEY -or $env:GEMINI_API_KEY)) {
    "[$(Get-Date -Format o)] ABORT: no GOOGLE_API_KEY/GEMINI_API_KEY in environment." | Tee-Object -FilePath $LogFile -Append
    exit 1
}

$uvDir = (uv tool dir 2>$null)
$Python = Join-Path $uvDir "graphifyy\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    "[$(Get-Date -Format o)] ABORT: graphify python interpreter not found at $Python" | Tee-Object -FilePath $LogFile -Append
    exit 1
}

"[$(Get-Date -Format o)] Starting graphify weekly update" | Tee-Object -FilePath $LogFile -Append

$pyScript = @'
import json, sys
from pathlib import Path
from graphify.detect import detect, save_manifest
from graphify.extract import collect_files, extract
from graphify.cache import check_semantic_cache, save_semantic_cache
from graphify.llm import extract_corpus_parallel
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.analyze import god_nodes, surprising_connections, suggest_questions
from graphify.report import generate
from graphify.export import to_json

scope = ["monitor", "config", "reports", "CLAUDE.md"]
out = Path("graphify-out")
out.mkdir(exist_ok=True)

# 1. detect (merged across scoped paths)
merged = {"files": {"code": [], "document": [], "paper": [], "image": [], "video": []}}
total_words = 0
for p in scope:
    r = detect(Path(p))
    for k, v in r.get("files", {}).items():
        merged["files"].setdefault(k, []).extend(v)
    total_words += r.get("total_words", 0)
merged["total_files"] = sum(len(v) for v in merged["files"].values())
merged["total_words"] = total_words
merged["scan_root"] = str(Path(".").resolve())

# 2. AST extract (code files - free)
code_files = []
for f in merged["files"].get("code", []):
    code_files.extend(collect_files(Path(f)) if Path(f).is_dir() else [Path(f)])
ast = extract(code_files, cache_root=Path(".")) if code_files else {"nodes": [], "edges": [], "input_tokens": 0, "output_tokens": 0}

# 3. semantic extract via Gemini (headless, no agent needed)
all_files = [Path(f) for files in merged["files"].values() for f in files]
cached_nodes, cached_edges, cached_hyper, uncached = check_semantic_cache(all_files)
new_nodes, new_edges, new_hyper = [], [], []
input_tok, output_tok = 0, 0
if uncached:
    sem_new = extract_corpus_parallel([Path(f) for f in uncached], backend="gemini", root=Path("."))
    new_nodes = sem_new.get("nodes", [])
    new_edges = sem_new.get("edges", [])
    new_hyper = sem_new.get("hyperedges", [])
    input_tok = sem_new.get("input_tokens", 0)
    output_tok = sem_new.get("output_tokens", 0)
    save_semantic_cache(new_nodes, new_edges, new_hyper)

sem_nodes = cached_nodes + new_nodes
sem_edges = cached_edges + new_edges
sem_hyper = cached_hyper + new_hyper

# 4. merge AST + semantic
seen = {n["id"] for n in ast["nodes"]}
merged_nodes = list(ast["nodes"])
for n in sem_nodes:
    if n["id"] not in seen:
        merged_nodes.append(n)
        seen.add(n["id"])
extraction = {
    "nodes": merged_nodes,
    "edges": ast["edges"] + sem_edges,
    "hyperedges": sem_hyper,
    "input_tokens": input_tok,
    "output_tokens": output_tok,
}

if not extraction["nodes"]:
    print("ERROR: empty extraction - aborting, previous graph.json left untouched")
    sys.exit(1)

# 5. build + cluster
G = build_from_json(extraction, root=".", directed=True)
communities = cluster(G)
cohesion = score_all(G, communities)
gods = god_nodes(G)
surprises = surprising_connections(G, communities)
labels = {cid: f"Community {cid}" for cid in communities}
questions = suggest_questions(G, communities, labels)

report = generate(G, communities, cohesion, labels, gods, surprises, merged,
                   {"input": input_tok, "output": output_tok}, ".", suggested_questions=questions)
Path("graphify-out/GRAPH_REPORT.md").write_text(report, encoding="utf-8")
to_json(G, communities, "graphify-out/graph.json")
save_manifest(merged["files"])

print(f"Graph updated: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, "
      f"{input_tok} in / {output_tok} out tokens, {len(uncached)} files re-extracted")
'@

$pyScript | & $Python -

if ($LASTEXITCODE -ne 0) {
    "[$(Get-Date -Format o)] FAILED - see output above" | Tee-Object -FilePath $LogFile -Append
    exit 1
}

# label communities + regenerate report (uses GOOGLE_API_KEY automatically)
& graphify label . --backend gemini 2>&1 | Tee-Object -FilePath $LogFile -Append

# refresh exports
& graphify export obsidian --dir "$VaultDir" 2>&1 | Tee-Object -FilePath $LogFile -Append
& graphify export html 2>&1 | Tee-Object -FilePath $LogFile -Append

# commit graph.json + report back to the repo (vault export stays local-only, untracked)
git add graphify-out/graph.json graphify-out/GRAPH_REPORT.md graphify-out/manifest.json graphify-out/cost.json 2>&1 | Out-Null
git diff --cached --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "graphify: weekly knowledge graph update" 2>&1 | Tee-Object -FilePath $LogFile -Append
    git push 2>&1 | Tee-Object -FilePath $LogFile -Append
}

"[$(Get-Date -Format o)] Done" | Tee-Object -FilePath $LogFile -Append

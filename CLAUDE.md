# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## GitHub Repository

**URL:** https://github.com/wakandalh-creator/ProjetoClaudecode

### Auto-sync

Every file created or edited via Claude Code is automatically committed and pushed to GitHub via a `PostToolUse` hook configured in `.claude/settings.local.json`.

The hook runs `.claude/auto-sync.ps1` after every `Write` or `Edit` tool call. The script:
1. Checks for uncommitted changes (`git status --porcelain`)
2. Stages all changes (`git add -A`)
3. Commits with a timestamp message (`Auto-sync: YYYY-MM-DD HH:mm:ss`)
4. Pushes to `origin HEAD`

### Manual sync

To push manually from a terminal:

```powershell
git add -A
git commit -m "sua mensagem"
git push
```

## Configuration

Claude Code settings and the auto-sync script are in `.claude/`. The file `.claude/settings.local.json` is excluded from git (via `.gitignore`) since it may contain local-only permissions.

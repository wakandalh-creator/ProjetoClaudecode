# Lightweight daily Obsidian sync for ProjetoClaudecode.
# Does NOT re-extract or call any LLM - only pulls the graph.json that the
# cloud routine (graphify-cloud-update, runs ~30min earlier) already
# rebuilt and committed, then re-renders the Obsidian vault from it.
# Uses only public, documented graphify CLI commands - no internal Python API.

$ErrorActionPreference = "Stop"
$ProjectRoot = "C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode"
$VaultDir    = "C:\Users\lucas\OneDrive\Área de Trabalho\Cerebro Claude\Codigo"
$LogFile     = Join-Path $ProjectRoot ".claude\scripts\graphify-obsidian-sync.log"

Set-Location $ProjectRoot
"[$(Get-Date -Format o)] Starting Obsidian sync" | Tee-Object -FilePath $LogFile -Append

git pull --ff-only 2>&1 | Tee-Object -FilePath $LogFile -Append

if (-not (Test-Path "graphify-out\graph.json")) {
    "[$(Get-Date -Format o)] SKIP: no graphify-out/graph.json yet (cloud routine hasn't run)" | Tee-Object -FilePath $LogFile -Append
    exit 0
}

& graphify export obsidian --dir "$VaultDir" 2>&1 | Tee-Object -FilePath $LogFile -Append
& graphify export html 2>&1 | Tee-Object -FilePath $LogFile -Append

"[$(Get-Date -Format o)] Done" | Tee-Object -FilePath $LogFile -Append

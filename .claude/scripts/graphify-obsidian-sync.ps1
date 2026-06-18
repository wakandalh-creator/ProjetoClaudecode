# Lightweight daily Obsidian sync for ProjetoClaudecode.
# Does NOT re-extract or call any LLM - only pulls the graph.json that the
# cloud routine (graphify-cloud-update, runs ~30min earlier) already
# rebuilt and committed, then re-renders the Obsidian vault from it.
# Uses only public, documented graphify CLI commands - no internal Python API.

$ProjectRoot = "C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode"
$VaultDir    = "C:\Users\lucas\OneDrive\Área de Trabalho\Cerebro Claude\Codigo"
$LogFile     = Join-Path $ProjectRoot ".claude\scripts\graphify-obsidian-sync.log"

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

# Native exes (git, graphify) write normal progress info to stderr. Redirecting
# it with 2>&1 makes PowerShell 5.1 wrap each line as a NativeCommandError and
# flip $? to false even on success - so each call is logged via Out-String
# instead, and only $LASTEXITCODE decides success/failure.
#
# PowerShell 5.1 decodes a non-interactive native process's output using the
# console's legacy codepage, mangling any accented character (e.g. paths
# under "Área de Trabalho") regardless of $OutputEncoding/[Console]::OutputEncoding
# settings. Rather than fight that, strip to ASCII before logging - the log is
# for a pass/fail glance, not for reading file paths (those are verified by
# checking the vault folder directly, not the log).
function Invoke-Logged {
    param([string]$Cmd, [string[]]$CmdArgs)
    $output = & $Cmd @CmdArgs 2>&1 | Out-String
    $ascii = [System.Text.Encoding]::ASCII.GetString([System.Text.Encoding]::ASCII.GetBytes($output))
    $ascii.TrimEnd() | Add-Content -Path $LogFile -Encoding utf8
    return $LASTEXITCODE
}

Set-Location $ProjectRoot
"[$(Get-Date -Format o)] Starting Obsidian sync" | Add-Content -Path $LogFile -Encoding utf8

$exit = Invoke-Logged "git" @("pull", "--ff-only")
if ($exit -ne 0) {
    "[$(Get-Date -Format o)] WARN: git pull exited $exit - continuing with whatever is on disk" | Add-Content -Path $LogFile -Encoding utf8
}

if (-not (Test-Path "graphify-out\graph.json")) {
    "[$(Get-Date -Format o)] SKIP: no graphify-out/graph.json yet (cloud routine hasn't run)" | Add-Content -Path $LogFile -Encoding utf8
    exit 0
}

Invoke-Logged "graphify" @("export", "obsidian", "--dir", $VaultDir) | Out-Null
Invoke-Logged "graphify" @("export", "html") | Out-Null

"[$(Get-Date -Format o)] Done" | Add-Content -Path $LogFile -Encoding utf8

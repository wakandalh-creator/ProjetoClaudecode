param()
# MCP Health Check - Diagnostico preventivo dos MCPs do Claude Code
# Criado em: 2026-07-08
# Uso: powershell -File .claude/scripts/mcp-health-check.ps1

$OK   = "[OK]   "
$WARN = "[AVISO]"
$ERR  = "[ERRO] "
$issues = 0

Write-Host ""
Write-Host "===== MCP Health Check =====" -ForegroundColor Cyan
Write-Host "Data: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

# 1. Node.js / npx
Write-Host "--- Node.js / npx ---"
$nvmPath = "C:\Users\lucas\AppData\Local\nvm\v24.15.0"
$npxFile = "$nvmPath\npx.cmd"
if (Test-Path $npxFile) {
    $ver = & "$nvmPath\node.exe" --version 2>$null
    Write-Host "$OK npx encontrado em $nvmPath (Node $ver)"
} else {
    Write-Host "$ERR npx NAO encontrado em $nvmPath" -ForegroundColor Red
    Write-Host "        Fix: verificar se nvm v24.15.0 ainda esta instalado"
    $issues++
}

# 2. uvx
Write-Host ""
Write-Host "--- uvx (sequential-thinking) ---"
$uvxCandidates = @(
    "C:\Users\lucas\.local\bin\uvx.exe",
    "$env:LOCALAPPDATA\uv\bin\uvx.exe",
    "$env:USERPROFILE\.local\bin\uvx.exe"
)
$uvBin = $uvxCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($uvBin) {
    Write-Host "$OK uvx encontrado: $uvBin"
} else {
    Write-Host "$ERR uvx NAO encontrado" -ForegroundColor Red
    Write-Host "        Fix: irm https://astral.sh/uv/install.ps1 | iex"
    $issues++
}

# 3. Cache sequential-thinking
Write-Host ""
Write-Host "--- Cache sequential-thinking ---"
$stCommit = "527ba64d86b68c4ca54f7986b65537ded19510fa"
$cacheDir = "$env:LOCALAPPDATA\uv\cache\archive-v0"
$stCache = Get-ChildItem $cacheDir -ErrorAction SilentlyContinue | Where-Object {
    (Test-Path "$($_.FullName)\Scripts\mcp-sequential-thinking.exe") -or
    (Test-Path "$($_.FullName)\Lib\site-packages\mcp_sequential_thinking")
}
if ($stCache) {
    Write-Host "$OK Cache encontrado ($($stCache.Count) entrada(s))"
} else {
    Write-Host "$WARN Cache nao encontrado - proximo startup fara download" -ForegroundColor Yellow
}

$mcpJson = "C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode\.mcp.json"
if (Test-Path $mcpJson) {
    $mcpContent = Get-Content $mcpJson -Raw
    if ($mcpContent -match $stCommit) {
        Write-Host "$OK .mcp.json com commit pinado corretamente"
    } elseif ($mcpContent -match "sequential-thinking") {
        Write-Host "$WARN sequential-thinking sem commit pinado - pode demorar 26s no startup" -ForegroundColor Yellow
        $issues++
    }
}

# 4. PATH no settings.json
Write-Host ""
Write-Host "--- PATH no settings.json global ---"
$settingsPath = "C:\Users\lucas\.claude\settings.json"
if (Test-Path $settingsPath) {
    $settingsContent = Get-Content $settingsPath -Raw
    if ($settingsContent -match "nvm") {
        Write-Host "$OK PATH com nvm configurado no settings.json"
    } else {
        Write-Host "$ERR PATH do nvm NAO encontrado no settings.json" -ForegroundColor Red
        Write-Host "        Fix: adicionar nvm\v24.15.0 na secao env.PATH"
        $issues++
    }
}

# 5. Versao da extensao VSCode
Write-Host ""
Write-Host "--- Extensao VSCode ---"
$exts = Get-ChildItem "$env:USERPROFILE\.vscode\extensions" -Filter "anthropic.claude-code-*" -ErrorAction SilentlyContinue | Sort-Object Name -Descending
if ($exts) {
    Write-Host "$OK Instalada: $($exts[0].Name)"
    if ($exts.Count -gt 2) {
        Write-Host "$WARN $($exts.Count) versoes antigas - considere remover as mais velhas" -ForegroundColor Yellow
    }
} else {
    Write-Host "$ERR Extensao Claude Code nao encontrada" -ForegroundColor Red
    $issues++
}

# 6. Logs MCP da ultima sessao
Write-Host ""
Write-Host "--- Logs MCP (ultima sessao) ---"
$logsBase = "$env:LOCALAPPDATA\claude-cli-nodejs\Cache\C--Users-lucas-OneDrive-Documentos-ProjetoClaudecode"
if (Test-Path $logsBase) {
    $mcpLogs = Get-ChildItem $logsBase -Filter "mcp-logs-*" -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 6
    $logErrs = 0
    foreach ($logDir in $mcpLogs) {
        $logFile = Get-ChildItem $logDir.FullName -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($logFile) {
            $lc = Get-Content $logFile.FullName -Raw -ErrorAction SilentlyContinue
            if ($lc -match "nao e reconhecido|Connection failed.*-32000") {
                Write-Host "$ERR $($logDir.Name): falha de conexao" -ForegroundColor Red
                $logErrs++
            } else {
                Write-Host "$OK $($logDir.Name)"
            }
        }
    }
    if ($logErrs -gt 0) { $issues++ }
} else {
    Write-Host "$WARN Pasta de logs nao encontrada"
}

# 7. Crashes no Event Viewer (ultimas 24h)
Write-Host ""
Write-Host "--- Crashes recentes (Event Viewer, 24h) ---"
$crashes = Get-WinEvent -LogName Application -ErrorAction SilentlyContinue | Where-Object {
    $_.Id -eq 1000 -and
    $_.TimeCreated -gt (Get-Date).AddHours(-24) -and
    $_.Message -match "node.exe|Code.exe|claude"
}
if ($crashes) {
    Write-Host "$ERR $($crashes.Count) crash(es) de Claude/VSCode detectados" -ForegroundColor Red
    $crashes | Select-Object -First 2 | ForEach-Object {
        $line = ($_.Message -split "`n" | Select-Object -First 2) -join " | "
        Write-Host "        $($_.TimeCreated): $line"
    }
    $issues++
} else {
    Write-Host "$OK Nenhum crash de Claude/VSCode nas ultimas 24h"
}

# Resumo final
Write-Host ""
Write-Host "============================" -ForegroundColor Cyan
if ($issues -eq 0) {
    Write-Host "RESULTADO: Tudo OK - nenhum problema encontrado" -ForegroundColor Green
} else {
    Write-Host "RESULTADO: $issues problema(s) encontrado(s) - veja os [ERRO] acima" -ForegroundColor Red
}
Write-Host ""

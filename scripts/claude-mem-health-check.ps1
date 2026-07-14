# claude-mem-health-check.ps1
# Diagnostico preventivo + auto-correcao do claude-mem no Windows.
# Uso manual:  pwsh -File scripts\claude-mem-health-check.ps1
# Uso agendado: Agendador de Tarefas do Windows -> Acao: pwsh.exe -File "C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode\scripts\claude-mem-health-check.ps1"
#
# Causa raiz historica (2026-07-13): shims orfaos do Bun instalados via npm
# (AppData\Roaming\npm\bun / bun.cmd / bun.ps1) tomavam precedencia no PATH
# sobre o binario real (.bun\bin\bun.exe), fazendo o worker do claude-mem
# cair num fallback que invocava node.exe -> "Cannot find module 'bun:sqlite'".
# Este script detecta e remove esse padrao automaticamente antes que ele volte a quebrar o worker.

$ErrorActionPreference = "Continue"
$logPrefix = "[claude-mem-health-check]"
$issuesFound = @()
$issuesFixed = @()

Write-Host "$logPrefix Iniciando verificacao $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor Cyan

# 1. Checar shims orfaos do Bun no PATH do npm
$npmBunPaths = @(
    "$env:APPDATA\npm\bun",
    "$env:APPDATA\npm\bun.cmd",
    "$env:APPDATA\npm\bun.ps1"
)
$foundOrphans = $npmBunPaths | Where-Object { Test-Path $_ }

if ($foundOrphans.Count -gt 0) {
    # So remove se NAO estiverem listados como pacote real do npm (protecao extra)
    $npmGlobalList = npm list -g --depth=0 2>$null
    $bunIsRealNpmPackage = $npmGlobalList -match "\bbun@"

    if (-not $bunIsRealNpmPackage) {
        $issuesFound += "Shims orfaos do Bun encontrados em AppData\Roaming\npm (mesmo padrao do bug de 2026-07-13)"
        foreach ($path in $foundOrphans) {
            Remove-Item $path -ErrorAction SilentlyContinue
        }
        $issuesFixed += "Shims orfaos do Bun removidos: $($foundOrphans -join ', ')"
        Write-Host "$logPrefix CORRIGIDO: shims orfaos do Bun removidos" -ForegroundColor Yellow
    } else {
        $issuesFound += "AVISO: 'bun' aparece como pacote npm real — NAO removido automaticamente, checar manualmente"
        Write-Host "$logPrefix ATENCAO: bun parece ser um pacote npm legitimo, pulei a remocao automatica" -ForegroundColor Red
    }
}

# 2. Confirmar que o Bun real resolve corretamente
$bunResolved = (Get-Command bun -ErrorAction SilentlyContinue).Source
if ($bunResolved -and $bunResolved -notlike "*.bun\bin\bun.exe") {
    $issuesFound += "Get-Command bun resolve para '$bunResolved' em vez do binario real em .bun\bin\bun.exe"
    Write-Host "$logPrefix ATENCAO: PATH ainda prioriza um shim/wrapper de Bun errado ($bunResolved)" -ForegroundColor Red
} else {
    Write-Host "$logPrefix OK: bun resolve para o binario real" -ForegroundColor Green
}

# 3. Rodar claude-mem doctor e capturar reparos automaticos possiveis
try {
    $doctorOutput = npx claude-mem doctor 2>&1 | Out-String
    if ($doctorOutput -match "node_modules missing") {
        Write-Host "$logPrefix Rodando 'npx claude-mem repair' (node_modules ausente)..." -ForegroundColor Yellow
        npx claude-mem repair 2>&1 | Out-Null
        $issuesFixed += "claude-mem repair executado (node_modules estava faltando)"
    }
    if ($doctorOutput -notmatch "All required checks passed") {
        $issuesFound += "claude-mem doctor NAO reportou 'All required checks passed' apos tentativa de reparo"
    } else {
        Write-Host "$logPrefix OK: claude-mem doctor - all required checks passed" -ForegroundColor Green
    }
} catch {
    $issuesFound += "Falha ao rodar 'npx claude-mem doctor': $($_.Exception.Message)"
}

# 4. Checar se o worker esta respondendo (porta configurada em settings.json, fallback 37777-37877)
$workerPort = $null
$settingsPath = "$env:USERPROFILE\.claude-mem\settings.json"
if (Test-Path $settingsPath) {
    try {
        $settings = Get-Content $settingsPath -Raw | ConvertFrom-Json
        $workerPort = $settings.CLAUDE_MEM_WORKER_PORT
    } catch {}
}

$portsToTry = @()
if ($workerPort) { $portsToTry += $workerPort }
$portsToTry += 37777..37877

$workerHealthy = $false
foreach ($port in $portsToTry) {
    try {
        $resp = Invoke-WebRequest -UseBasicParsing -Uri "http://127.0.0.1:$port/health" -TimeoutSec 1 -ErrorAction Stop
        if ($resp.StatusCode -eq 200) {
            $workerHealthy = $true
            Write-Host "$logPrefix OK: worker respondendo na porta $port" -ForegroundColor Green
            break
        }
    } catch {}
}

if (-not $workerHealthy) {
    $issuesFound += "Worker nao respondeu health check em nenhuma porta testada"
    Write-Host "$logPrefix ATENCAO: worker nao respondeu. Tentando 'npx claude-mem start'..." -ForegroundColor Yellow
    try {
        npx claude-mem start 2>&1 | Out-Null
        $issuesFixed += "npx claude-mem start executado (worker nao estava respondendo)"
    } catch {
        $issuesFound += "Falha ao rodar 'npx claude-mem start': $($_.Exception.Message)"
    }
}

# 5. Resumo
Write-Host ""
Write-Host "$logPrefix ===== RESUMO =====" -ForegroundColor Cyan
if ($issuesFound.Count -eq 0) {
    Write-Host "$logPrefix Nenhum problema encontrado. Tudo saudavel." -ForegroundColor Green
} else {
    Write-Host "$logPrefix Problemas encontrados:" -ForegroundColor Yellow
    $issuesFound | ForEach-Object { Write-Host "  - $_" -ForegroundColor Yellow }
}
if ($issuesFixed.Count -gt 0) {
    Write-Host "$logPrefix Correcoes aplicadas automaticamente:" -ForegroundColor Green
    $issuesFixed | ForEach-Object { Write-Host "  - $_" -ForegroundColor Green }
}

# Log persistente para auditoria
$logFile = "$env:USERPROFILE\.claude-mem\health-check-history.log"
$entry = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | Issues: $($issuesFound.Count) | Fixed: $($issuesFixed.Count) | $(($issuesFound + $issuesFixed) -join ' ;; ')"
Add-Content -Path $logFile -Value $entry

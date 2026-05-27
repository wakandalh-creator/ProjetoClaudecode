$env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH", "User")
Set-Location "C:\Users\lucas\OneDrive\Documentos\ProjetoClaudecode"

$status = git status --porcelain
if ($status) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git add -A
    git commit -m "Auto-sync: $timestamp"
    git push origin HEAD
}

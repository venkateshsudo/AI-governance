Set-Location -LiteralPath $PSScriptRoot

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host ""
    Write-Host "  Python 3 is required to run the local preview server." -ForegroundColor Yellow
    Write-Host "  Install it from https://www.python.org/downloads/ and try again."
    Write-Host ""
    Read-Host "Press Enter to close"
    exit 1
}

python serve.py @args

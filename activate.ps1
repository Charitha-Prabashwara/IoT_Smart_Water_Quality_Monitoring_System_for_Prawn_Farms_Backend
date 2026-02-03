$venv = ".venv\Scripts\Activate.ps1"

if (Test-Path $venv) {
    & $venv
} else {
    Write-Host ".venv not found. Run setup first."
}

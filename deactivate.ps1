
if (-not $env:VIRTUAL_ENV) {
    Write-Host "No virtual environment is currently active."
    return
}


if (Get-Command deactivate -ErrorAction SilentlyContinue) {
    deactivate
    Write-Host "Virtual environment deactivated."
} else {
    Write-Host "Deactivate function not found. Are you in a Python venv?"
}

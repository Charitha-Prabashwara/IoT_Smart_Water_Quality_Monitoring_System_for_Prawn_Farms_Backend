if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
& .venv\Scripts\Activate.ps1

if (Test-Path "requirements.txt") {
    Write-Host "Installing dependencies..."
    pip install -r requirements.txt
}

Write-Host "Done."

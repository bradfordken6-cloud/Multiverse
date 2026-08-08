$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')

if (-not (Test-Path '.env')) {
  Write-Host '[Omniverse] Creating .env from .env.example'
  Copy-Item '.env.example' '.env'
}

Write-Host '[Omniverse] Validating Compose configuration...'
docker compose config -q

Write-Host '[Omniverse] Starting the full stack...'
docker compose up -d --build --remove-orphans

Write-Host '[Omniverse] Stack status:'
docker compose ps
Write-Host '[Omniverse] API: http://localhost:8080/health'

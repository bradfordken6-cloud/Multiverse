$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
  throw 'Docker is required.'
}

docker compose up --build -d
Write-Host 'Omniverse is UP.'
Write-Host 'API: http://localhost:8080/health'
docker compose ps

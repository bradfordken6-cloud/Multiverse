#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

command -v docker >/dev/null 2>&1 || { echo "Docker is required."; exit 1; }
docker compose up --build -d

echo "Omniverse is UP."
echo "API: http://localhost:8080/health"
docker compose ps

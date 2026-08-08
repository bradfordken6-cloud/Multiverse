#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from .env.example. Review it before production use."
fi

echo "Starting Omniverse stack..."
docker compose -f omniverse/docker-compose.yml up --build -d

echo
echo "Omniverse stack is starting."
echo "API:          http://localhost:8080/health"
echo "Orchestrator: http://localhost:8090/health"
echo
docker compose -f omniverse/docker-compose.yml ps

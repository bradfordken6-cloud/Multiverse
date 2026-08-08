#!/usr/bin/env sh
set -eu

ROOT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT_DIR"

if [ ! -f .env ]; then
  echo "Creating .env from .env.example"
  cp .env.example .env
fi

echo "[Omniverse] Validating Compose configuration..."
docker compose config -q

echo "[Omniverse] Starting the full stack..."
docker compose up -d --build --remove-orphans

echo "[Omniverse] Stack status:"
docker compose ps

echo "[Omniverse] API: http://localhost:8080/health"

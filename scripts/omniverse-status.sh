#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
docker compose ps
printf '\nHealth:\n'
curl -fsS http://localhost:8080/health || true
printf '\n'

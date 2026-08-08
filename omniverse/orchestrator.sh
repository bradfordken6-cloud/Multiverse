#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

case "${1:-up}" in
  up)
    docker compose up --build -d
    docker compose ps
    ;;
  down)
    docker compose down
    ;;
  restart)
    docker compose down
    docker compose up --build -d
    docker compose ps
    ;;
  status)
    docker compose ps
    ;;
  logs)
    docker compose logs -f --tail=200
    ;;
  health)
    curl -fsS http://localhost:8080/health
    echo
    ;;
  *)
    echo "Usage: $0 {up|down|restart|status|logs|health}" >&2
    exit 2
    ;;
esac

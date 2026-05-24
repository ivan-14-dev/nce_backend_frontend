#!/usr/bin/env bash
set -euo pipefail

# Render web service: Django (Gunicorn)
# Expected working directory: repository root (we will cd)

cd "$(dirname "$0")"

export DJANGO_SETTINGS_MODULE="nce_backend_tmp.settings"
export PYTHONUNBUFFERED=1

PORT="${PORT:-8000}"

# Run gunicorn against the WSGI entrypoint
exec gunicorn nce_backend_tmp.wsgi:application \
  --bind "0.0.0.0:${PORT}" \
  --workers "${GUNICORN_WORKERS:-3}" \
  --timeout "${GUNICORN_TIMEOUT:-120}"

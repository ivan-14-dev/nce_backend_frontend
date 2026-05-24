#!/usr/bin/env bash
set -euo pipefail

# Render worker: Celery (emails automatiques)
# L’idée: démarrer à la fois worker + beat.
# (Render peut nécessiter des entrées séparées selon ton template, mais
# ce script fonctionne en single container.)

cd "$(dirname "$0")"

export DJANGO_SETTINGS_MODULE="nce_backend_tmp.settings"
export PYTHONUNBUFFERED=1

: "${CELERY_CONCURRENCY:=2}"
: "${CELERY_QUEUE:=default}"
: "${CELERY_LOGLEVEL:=INFO}"

# Beat scheduler (django-celery-beat)
celery -A nce_backend_tmp worker \
  --loglevel="${CELERY_LOGLEVEL}" \
  --concurrency="${CELERY_CONCURRENCY}" \
  -Q "${CELERY_QUEUE}" &

WORKER_PID=$!

celery -A nce_backend_tmp beat \
  --loglevel="${CELERY_LOGLEVEL}" &

wait "${WORKER_PID}"

import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nce_backend_tmp.settings")

app = Celery("nce_backend_tmp")

# Charger la config depuis settings.py avec le préfixe "CELERY_"
app.config_from_object("django.conf:settings", namespace="CELERY")

# Découvrir automatiquement les tâches dans les apps Django
app.autodiscover_tasks()

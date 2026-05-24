"""
WSGI config for nce_backend_tmp project.

Render/Gunicorn entrypoint.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nce_backend_tmp.settings")

application = get_wsgi_application()

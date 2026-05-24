"""
Shim celery module for legacy imports:
  nce_backend_frontend.nce_backend_tmp.celery

Redirects to the real module:
  nce_backend_tmp.celery
"""
from nce_backend_tmp.celery import *  # noqa: F401,F403

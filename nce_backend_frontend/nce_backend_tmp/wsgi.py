"""
Shim wsgi module for legacy imports:
  nce_backend_frontend.nce_backend_tmp.wsgi

Redirects to the real module:
  nce_backend_tmp.wsgi
"""
from nce_backend_tmp.wsgi import *  # noqa: F401,F403

"""
Shim package for legacy Gunicorn import paths.

Some Render deploys may try to import:
  nce_backend_frontend.nce_backend_tmp.wsgi

This package re-exports the real Django project package `nce_backend_tmp`.
"""

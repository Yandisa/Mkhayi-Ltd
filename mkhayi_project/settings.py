"""
mkhayi_project/settings.py — PRODUCTION-READY CHANGES
Replace the relevant lines in your existing settings.py with these.
All changes are marked with # <-- UPDATED
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------
# SECURITY — read from environment variables
# ------------------------------------------------------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-only-for-dev')  # <-- UPDATED

DEBUG = os.environ.get('DEBUG', 'False') == 'True'  # <-- UPDATED

ALLOWED_HOSTS = os.environ.get(
    'ALLOWED_HOSTS',
    'mkhayiltd.co.za,www.mkhayiltd.co.za'
).split(',')  # <-- UPDATED

# ------------------------------------------------------------------
# CSRF — required for forms to work behind HTTPS / reverse proxy
# ------------------------------------------------------------------
CSRF_TRUSTED_ORIGINS = os.environ.get(
    'CSRF_TRUSTED_ORIGINS',
    'https://mkhayiltd.co.za,https://www.mkhayiltd.co.za'
).split(',')  # <-- UPDATED (add this block if it doesn't exist)

# ------------------------------------------------------------------
# SECURE PROXY HEADERS — needed when sitting behind Coolify/Traefik
# ------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # <-- UPDATED (add if missing)
USE_X_FORWARDED_HOST = True  # <-- UPDATED (add if missing)

# ------------------------------------------------------------------
# DATABASE — SQLite path pointing to the persistent volume
# ------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db' / 'db.sqlite3',  # <-- UPDATED: stored in /app/db/ (volume mount)
    }
}

# ------------------------------------------------------------------
# STATIC & MEDIA
# ------------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

from .base import *

# Modo desarrollo
DEBUG = True

# Permitir localhost
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
SECRET_KEY = "django-insecure-esta-es-una-clave-de-desarrollo"
# Base de datos SQLite (la misma que en base.py)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Archivos estáticos y media (igual que base.py)
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
STATIC_ROOT = BASE_DIR / "static"
MEDIA_ROOT = BASE_DIR / "media"

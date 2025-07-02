from .base import *

DEBUG = False
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME":env("POSTGRES_DB"),
        "USER":env("POSTGRES_USER"),
        "PASSWORD":env("POSTGRES_PASSWORD"),
        "HOST":env("POSTGRES_HOST", default="db"),
        "PORT":env("POSTGRES_PORT", default="5432"),
    }
}

# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# CSRF_TRUSTED_ORIGINS    = env.list("DJANGO_CSRF_TRUSTED", default=[])

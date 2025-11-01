from .base import *

DEBUG = False

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[
    "https://geteverythinghere.com",
    "https://www.geteverythinghere.com",
])

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
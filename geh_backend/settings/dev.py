from .base import *

# SSL Disabled for development
# Console emial backedn for development
SECURE_SSL_REDIRECT = False
CRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
DEBUG = True
ALLOWED_HOSTS = ['*']
FRONTEND_URL = env.str("FRONTEND_URL", default="http://localhost:8000")

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:3000',
    'http://dev.geteverythinghere.com',
]

# from .base import *

# DEBUG = False

# CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[
#     "https://geteverythinghere.com",
#     "https://www.geteverythinghere.com",
# ])

# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True


"""
Production settings for geh_backend.
"""
from .base import *
import os

# ==================== PRODUCTION SETTINGS ====================
DEBUG = False

# ==================== SECURITY ====================
# Enable all security features
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
X_FRAME_OPTIONS = 'DENY'

# ==================== HOSTS ====================

if IS_RENDER and RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    
# Add custom domains
custom_domains = env.list("CUSTOM_DOMAINS", default=[])
ALLOWED_HOSTS.extend(custom_domains)

# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[
#     "geh-backend.onrender.com",
#     "www.geh-backend.onrender.com",
#     "gadget-pro-ghana-api.com",
#     "www.gadget-pro-ghana-api.com",
#     "localhost",  # For health checks
# ])

# ==================== CORS ====================
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[
    "https://your-frontend-domain.com",
    "https://www.your-frontend-domain.com",
    "https://gadget-pro-ghana.com",
    "https://www.gadget-pro-ghana.com",
])

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False  # Strict in production

CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS.copy()
if IS_RENDER and RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")

# ==================== DATABASE ====================
# Force PostgreSQL in production
DATABASES = {
    'default': dj_database_url.config(
        default=env.str("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True,
    )
}

# ==================== CLOUDINARY ====================
# Ensure Cloudinary is configured in production
if not CLOUDINARY_ENABLED:
    raise ValueError("Cloudinary credentials must be set in production")



# ==================== STATIC & MEDIA FILES ====================


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# # Force AWS S3 in production
# USE_AWS_S3 = True

# if not env.str("AWS_ACCESS_KEY_ID", default=None):
#     raise ValueError("AWS_ACCESS_KEY_ID must be set in production")

# if not env.str("AWS_SECRET_ACCESS_KEY", default=None):
#     raise ValueError("AWS_SECRET_ACCESS_KEY must be set in production")

# # Ensure AWS is configured
# AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default="gadget-pro-ghana-prod")
# AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", default="eu-west-2")
# AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
# AWS_DEFAULT_ACL = 'public-read'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_FILE_OVERWRITE = False

# Static files
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'

# # Media files
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# ==================== EMAIL ====================
# Use real email backend in production
if env.str("EMAIL_HOST", default=None):
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env.str("EMAIL_HOST")
    EMAIL_PORT = env.int("EMAIL_PORT", default=587)
    EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
    EMAIL_HOST_USER = env.str("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD")
    DEFAULT_FROM_EMAIL = env.str("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ==================== LOGGING ====================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'production.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# ==================== PERFORMANCE ====================
# Cache settings (optional - for production)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env.str("REDIS_URL", default="redis://127.0.0.1:6379/1"),
    }
}

# ==================== MONITORING ====================
# Optional: Add monitoring middleware
MIDDLEWARE.append('django.middleware.gzip.GZipMiddleware')

print("=" * 50)
print("RUNNING IN PRODUCTION MODE")
print(f"DEBUG: {DEBUG}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
print(f"CLOUDINARY ENABLED: {CLOUDINARY_ENABLED}")
print(f"RENDER HOSTNAME: {RENDER_EXTERNAL_HOSTNAME}")
print("=" * 50)
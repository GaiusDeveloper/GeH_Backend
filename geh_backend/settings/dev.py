# from .base import *

# # SSL Disabled for development
# # Console emial backedn for development
# SECURE_SSL_REDIRECT = False
# CRF_COOKIE_SECURE = False
# SESSION_COOKIE_SECURE = False
# DEBUG = True
# ALLOWED_HOSTS = ['*']
# FRONTEND_URL = env.str("FRONTEND_URL", default="http://localhost:8000")

# CSRF_TRUSTED_ORIGINS = [
#     'http://localhost:8000',
#     'http://127.0.0.1:3000',
#     'http://dev.geteverythinghere.com',
# ]



from .base import *
import os

# ==================== DEVELOPMENT SETTINGS ====================
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# ==================== SECURITY ====================
# Disable security for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

# ==================== CORS ====================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://dev.geteverythinghere.com',
]

# ==================== DATABASE ====================
# Use SQLite for development unless DATABASE_URL is set
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        "default": dj_database_url.config(default=os.environ.get('DATABASE_URL'), conn_max_age=600, ssl_require=False)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ==================== STATIC & MEDIA FILES ====================
# Local static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==================== EMAIL ====================
# Use console backend for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ==================== STATIC FILES ====================
# Use local storage for development
USE_AWS_S3 = env.bool("USE_AWS_S3", default=False)

# Local media files (if not using Cloudinary)
if not CLOUDINARY_ENABLED:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ==================== LOGGING ====================
LOGGING['loggers']['django']['level'] = 'DEBUG'
LOGGING['loggers']['django.db.backends'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
}

print("=" * 50)
print("RUNNING IN DEVELOPMENT MODE")
print(f"DEBUG: {DEBUG}")
print(f"ALLOWED_HOSTS: {ALLOWED_HOSTS}")
print("=" * 50)

# ==================== DJANGO DEBUG TOOLBAR ====================
# Optional: Add django-debug-toolbar for development
# try:
#     import debug_toolbar
#     INSTALLED_APPS.append('debug_toolbar')
#     MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    
#     INTERNAL_IPS = [
#         '127.0.0.1',
#         'localhost',
#     ]
    
#     DEBUG_TOOLBAR_CONFIG = {
#         'SHOW_TOOLBAR_CALLBACK': lambda request: True,
#     }
# except ImportError:
#     pass

# print("=" * 50)
# print("RUNNING IN DEVELOPMENT MODE")
# print("DEBUG: True")
# print("ALLOWED_HOSTS: *")
# print("=" * 50)
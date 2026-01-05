# ##Import packages and modules
# import os
# from pathlib import Path
# from environs import Env
# import dj_database_url
# from datetime import timedelta


# #instance of Env
# env = Env()
# env.read_env()


# BASE_DIR = Path(__file__).resolve().parent.parent.parent


# # SECURITY SETTINGS
# SECRET_KEY = env.str("SECRET_KEY", "fallback-secret-dev")
# DEBUG = env.bool("DEBUG", default = False)
# PORT = os.environ.get('PORT', 8000)
# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])
# SITE_ID  = 1

# # INstalled apps
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django.contrib.sites',

#     # Third party
#     'rest_framework',
#     'rest_framework.authtoken',
#     'rest_framework_simplejwt',
#     'dj_rest_auth',
#     # 'dj_rest_auth.jwt_auth',
#     'dj_rest_auth.registration',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'drf_yasg',
#     'anymail',
#     "corsheaders",
#     'cloudinary',
#     'cloudinary_storage',
#     'django_filters',

#     # Local
#     'post_api',
# ]


# # middleware
# MIDDLEWARE = [
#     "corsheaders.middleware.CorsMiddleware",
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'allauth.account.middleware.AccountMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


# # URL Configuration
# ROOT_URLCONF = 'geh_backend.urls'

# # Templates
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'geh_backend.wsgi.application'

# # Database
# if env.str("DATABASE_URL", default=None):
#     DATABASES = {
#         "default": dj_database_url.parse(
#             env.str("DATABASE_URL"),
#             conn_max_age=600,
#         )
#     }
# else:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": BASE_DIR / "db.sqlite3",
#         }
#     }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {"NAME": 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {"NAME": 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {"NAME": 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {"NAME": 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# # Language and Timezones
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # ==================== STATIC & MEDIA FILES ====================
# # AWS S3 Configuration for static and media files
# USE_AWS_S3 = env.bool("USE_AWS_S3", default=False)

# if USE_AWS_S3 and env.str("AWS_ACCESS_KEY_ID", default=None) and env.str("AWS_SECRET_ACCESS_KEY", default=None):
#     # Add storages to INSTALLED_APPS if using AWS
#     INSTALLED_APPS.append('storages')
    
#     # Configure AWS S3
#     AWS_ACCESS_KEY_ID = env.str("AWS_ACCESS_KEY_ID")
#     AWS_SECRET_ACCESS_KEY = env.str("AWS_SECRET_ACCESS_KEY")
#     AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default="gadget-pro-ghana")
#     AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", default="eu-west-2")  # London region
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
#     AWS_S3_OBJECT_PARAMETERS = {
#         'CacheControl': 'max-age=86400',
#     }
#     AWS_LOCATION = 'static'
#     AWS_DEFAULT_ACL = 'public-read'
#     AWS_QUERYSTRING_AUTH = False
#     AWS_S3_FILE_OVERWRITE = False
    
#     # Static files configuration
#     STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    
#     # Media files configuration
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
#     MEDIA_ROOT = ''  # Not used when using S3
    
#     # Ensure staticfiles finds static files properly
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static'),
#     ]
# else:
#     # Local static and media files
#     STATIC_URL = '/static/'
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static'),
#     ]
    
#     MEDIA_URL = '/media/'
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
#     # Use Whitenoise for static files
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#     WHITENOISE_USE_FINDERS = True
#     WHITENOISE_MANIFEST_STRICT = False
#     WHITENOISE_ALLOW_ALL_ORIGINS = True





# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.AllowAny',
#         ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#         'rest_framework.authentication.BasicAuthentication',
#     ],
#     'DEFAULT_FILTERS_BACKENDS': [
#         'django_filters.rest_framework.DjangoFilterBackends',
#         ],
#     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 10,
# }

# # ==================== JWT AUTHENTICATION ====================
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,
#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,
#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
#     'JTI_CLAIM': 'jti',
#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }

# REST_AUTH ={
#     'USE_JWT': True,
# }
# REST_USE_JWT = False

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }

# # ==================== DJ-REST-AUTH ====================
# REST_AUTH = {
#     'USE_JWT': True,
#     'JWT_AUTH_COOKIE': 'access',
#     'JWT_AUTH_REFRESH_COOKIE': 'refresh',
#     'JWT_AUTH_HTTPONLY': False,
#     'SESSION_LOGIN': False,
#     'OLD_PASSWORD_FIELD_ENABLED': True,
#     'LOGOUT_ON_PASSWORD_CHANGE': False,
# }

# DJ_REST_AUTH = {
#     "USE_JWT": True,
#     "JWT_AUTH_HTTPONLY": False,
#     "JWT_AUTH_REFRESH_COOKIE": "refresh-token",
#     "JWT_AUTH_COOKIE": "access-token",
#     "JWT_AUTH_COOKIE_USE_CSRF": False,
#     "JWT_AUTH_SECURE": not DEBUG,
#     "USER_DETAILS_SERIALIZER": "dj_rest_auth.serializers.UserDetailsSerializer",
# }

# REST_USE_JWT = True

# # DJ_REST_AUTH = {
# #     "USE_JWT": True,
# #     "JWT_AUTH_HTTPONLY": False,
# # }




# # Authentication backends

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# )

# ACCOUNT_LOGIN_METHODS = {'username', 'email'}
# ACCOUNT_SIGNUP_FIELD = ['username*', 'email*', 'password1*', 'password2*']
# ACCOUNT_EMAIL_VERIFICATION = 'optional'
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_SESSION_REMEMBER = True
# ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_USERNAME_REQUIRED = True
# LOGIN_REDIRECT_URL = '/'



# # Email configuration
# EMAIL_BACKEND = env.str("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
# EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
# EMAIL_PORT = env.int("EMAIL_PORT", default=587)
# EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
# EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
# EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# # ==================== CORS ====================
# CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ])
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_ALL_ORIGINS = DEBUG  # Only allow all origins in DEBUG mode

# # ==================== SWAGGER ====================
# SWAGGER_SETTINGS = {
#     'USE_SESSION_AUTH': False,
#     'SECURITY_DEFINITIONS': {
#         'Bearer': {
#             'type': 'apiKey',
#             'name': 'Authorization',
#             'in': 'header',
#         },
#     },
#     'DEFAULT_INFO': 'geh_backend.urls.api_info',
# }

# # ==================== CLOUDINARY ====================
# if env.str("CLOUDINARY_CLOUD_NAME", default=None):
#     CLOUDINARY_STORAGE = {
#         'CLOUD_NAME': env.str("CLOUDINARY_CLOUD_NAME"),
#         'API_KEY': env.str("CLOUDINARY_API_KEY"),
#         'API_SECRET': env.str("CLOUDINARY_API_SECRET"),
#     }
#     DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# # ==================== DEFAULT AUTO FIELD ====================
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # ==================== LOGGING ====================
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'debug.log'),
#             'formatter': 'verbose',
#         },
#     },
#     'root': {
#         'handlers': ['console'],
#         'level': 'WARNING',
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': env.str('DJANGO_LOG_LEVEL', 'INFO'),
#             'propagate': False,
#         },
#     },
# }


import os
from pathlib import Path
import dj_database_url
from datetime import timedelta
import environ
from geh_backend.settings import BASE_DIR

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env()


# SECURITY SETTINGS
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
SITE_ID = 1

# Render-specific configuration
IS_RENDER = env.bool("IS_RENDER", default=False)
RENDER_EXTERNAL_HOSTNAME = env.str("RENDER_EXTERNAL_HOSTNAME", "")
if IS_RENDER:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Third party
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'drf_yasg',
    'anymail',
    "corsheaders",
    'cloudinary',
    'cloudinary_storage',
    'django_filters',
    'storages',  # For static files on Render

    # Local
    'post_api',
]

# MIDDLEWARE
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For static files on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL Configuration
ROOT_URLCONF = 'geh_backend.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geh_backend.wsgi.application'

# DATABASE - Configured for Neon PostgreSQL
# Use DATABASE_URL from Render environment variables
DATABASES = {
    'default': dj_database_url.config(
        default=env.str('DATABASE_URL', 'sqlite:///db.sqlite3'),
        conn_max_age=600,
        conn_health_checks=True,
        ssl_require=env.bool('DATABASE_SSL_REQUIRE', default=True),
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {"NAME": 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {"NAME": 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {"NAME": 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Language and Timezones
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==================== STATIC & MEDIA FILES ====================
# Static files configuration for Render
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # Use Whitenoise for static files on Render


# ==================== MEDIA FILES - CLOUDINARY ====================
# Cloudinary configuration
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env.str('CLOUDINARY_CLOUD_NAME', 'djq3f4f4n'),
    'API_KEY': env.str('CLOUDINARY_API_KEY', '735995278464948'),
    'API_SECRET': env.str('CLOUDINARY_API_SECRET', 'C0IdRtJLt81xveJWi9Y4PvMLe8XA'),
}

# ONly use cloudinary if credentials are provided
CLOUDINARY_ENABLED = all([
    env.str('CLOUDINARY_CLOUD_NAME', default=None),
    env.str('CLOUDINARY_API_KEY', default=None),
    env.str('CLOUDINARY_API_SECRET', default=None),
])

# Use Cloudinary for media files
if CLOUDINARY_ENABLED:
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    MEDIA_URL = '/media/'  # Cloudinary will handle the actual URLs
else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# JWT Configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

# DJ-REST-AUTH Configuration
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'access',
    'JWT_AUTH_REFRESH_COOKIE': 'refresh',
    'JWT_AUTH_HTTPONLY': True,
    'JWT_AUTH_SAMESITE': 'Lax',
    'SESSION_LOGIN': False,
    'OLD_PASSWORD_FIELD_ENABLED': True,
    'LOGOUT_ON_PASSWORD_CHANGE': False,
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
}

# Allauth Configuration
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory' if not DEBUG else 'optional'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'

# Authentication backends
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Email Configuration (Updated for Render)
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # For production, use a proper email service
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = env.str('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_PORT = env.int('EMAIL_PORT', 587)
    EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', True)
    EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# CORS Configuration
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
])

# Add your frontend domain when deployed
FRONTEND_URL = env.str("FRONTEND_URL", "")
if FRONTEND_URL:
    CORS_ALLOWED_ORIGINS.append(FRONTEND_URL)

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Only allow all origins in DEBUG mode

# CSRF Configuration for Render
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS.copy()
if FRONTEND_URL:
    CSRF_TRUSTED_ORIGINS.append(FRONTEND_URL)
if IS_RENDER and RENDER_EXTERNAL_HOSTNAME:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RENDER_EXTERNAL_HOSTNAME}")

# Swagger Settings
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
        },
    },
    'DEFAULT_INFO': 'geh_backend.urls.api_info',
}

# Security settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging Configuration for Render
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
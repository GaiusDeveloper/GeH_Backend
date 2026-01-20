##Import packages and modules
import os
from pathlib import Path
from environs import Env
from datetime import timedelta
import cloudinary
import cloudinary.uploader
import cloudinary.api



#instance of Env
env = Env()
env.read_env()


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY SETTINGS
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default = False)

PORT = int(os.environ.get('PORT', 8000))

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

SITE_ID  = 1

# INstalled apps
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

    # Local
    'post_api',
]


# middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
        'DIRS': [],
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

# DATABASE
DATABASES = {"default": env.dj_db_url('DATABASE_URL')}

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

# # ==================== STATIC & MEDIA FILES ====================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# static_path = BASE_DIR / 'static'
# STATICFILES_DIRS = [static_path] if static_path.exists() else []

STORAGES = {
     "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage",
    }

}


REST_USE_JWT = True
TOKEN_MODEL = None

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTERS_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackends',
        ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}



# ==================== JWT AUTHENTICATION ====================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# ==================== DJ-REST-AUTH ====================
DJ_REST_AUTH = {
    "USE_JWT": True,
    
    "JWT_AUTH_HTTPONLY": False,
    "JWT_AUTH_COOKIE_USE_CSRF": False,
    
    # NO cookies used only JWT
    "JWT_AUTH_REFRESH_COOKIE": None,
    "JWT_AUTH_COOKIE": None,
    
    # "JWT_AUTH_SECURE": not DEBUG,
    "USER_DETAILS_SERIALIZER": "dj_rest_auth.serializers.UserDetailsSerializer",
}


# Authentication backends

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Login: USername onyl
ACCOUNT_LOGIN_METHODS = {'username'}

# SIgnup: required username + email
ACCOUNT_SIGNUP_FIELDS = {
    'email': {
        'required': True,
        'max_length': 254,
    },
    # Add other fields as needed
    'username': {
        'required': True,  # or True based on your needs
        'max_length': 150,
    },
    'password1': {
        'required': True,
    },
    'password2': {
        'required': True,
    },
}
# No email-verification
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_UNIQUE_EMAIL = True

# Session
ACCOUNT_SESSION_REMEMBER = True
LOGIN_REDIRECT_URL = '/'



# Email configuration
EMAIL_BACKEND = env.str("EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend")
EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# ==================== CLOUDINARY ====================
MEDIA_URL = '/media/'
# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# ==================== CORS ====================
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = DEBUG  # Only allow all origins in DEBUG mode

# ==================== SWAGGER ====================
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




# ==================== DEFAULT AUTO FIELD ====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== LOGGING ====================
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
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': env.str('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}

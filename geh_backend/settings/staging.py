# Configuration for staging environment
from .base import *

DEBUG = False

CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["https://staging.geteverythinghere.com"])

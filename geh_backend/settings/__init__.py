import os
from pathlib import Path
import environ


# instance of Env
#Initialize environs first
env = environ.Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env file before importing any settings
env_file = BASE_DIR / '.env'
if env_file.exists():
    environ.Env.read_env(str(env_file))


# Determine environment from env variable (not os.getenv yet)
# We need to use env() since environ is already loaded
environment = env.str('ENVIRONMENT', 'dev')


# Import appropriate settings based on environment
if environment == "prod":
    from .prod import *
else:
    from .dev import *

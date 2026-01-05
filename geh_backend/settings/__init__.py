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
    print(f"Loading base environment from {env_file}")
    environ.Env.read_env(str(env_file))
else:
    print(f"No .env file found at {env_file}")


# Determine environment from env variable (not os.getenv yet)
# We need to use env() since environ is already loaded
environment = os.environ.get('ENVIRONMENT', 'dev')
print(f"Detected environment: {environment}")

env_file_specific = BASE_DIR / f'.env.{environment}'
if env_file_specific.exists():
    print(f"Loading environment-specific settings from {env_file_specific}")
    environ.Env.read_env(str(env_file_specific))
else:
    print(f"No environment-specific .env file found at {env_file_specific}")


# Import appropriate settings based on environment
if environment == "prod":
    print("Using production settings")
    from .prod import *
else:
    print("Using development settings")
    from .dev import *

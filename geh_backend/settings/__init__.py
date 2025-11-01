import os
env = os.getenv('ENVIRONMENT', 'dev')

if env == "prod":
    from .prod import *
elif env == "staging":
    from .staging import *
else:
    from .dev import *
    
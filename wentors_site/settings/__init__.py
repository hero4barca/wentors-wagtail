import os

if os.environ.get("ENV_NAME") == 'production':
    from .production import *
elif os.environ.get("ENV_NAME") == 'staging':
    from .production import *
else:
    from .dev import *
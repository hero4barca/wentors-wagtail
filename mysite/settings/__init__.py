if os.environ.get("ENV_NAME") == 'Production':
    from .production import *
else:
    from .dev import *
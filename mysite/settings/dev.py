from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# installed apps for dev only
INSTALLED_APPS += [

]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x)tex3$f&+*c3qd9y0j^)y!fby**k9*2&^wq46^4ycw4+n_)js'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



try:
    from .local import *
except ImportError:
    pass

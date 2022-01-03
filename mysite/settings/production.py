from .base import *

# turn debug to false in production
DEBUG = False

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# set to use postgre backend in production
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite_db',
    }
}

try:
    from .local import *
except ImportError:
    pass

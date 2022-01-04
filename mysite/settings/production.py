from .base import *
import dj_database_url

# turn debug to false in production
DEBUG = False

# read secret key from environment variable
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") 

	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# set to use postgre backend in production



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myiste_db',
    }
}
DATABASES['default'] = dj_database_url.config()

try:
    from .local import *
except ImportError:
    pass

from .base import *


import dj_database_url # postgre db_url


# turn debug to false in production
DEBUG = True

# installed apps for prod only
INSTALLED_APPS += [

]

# read secret key from environment variable
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") 

	
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# redirect all non secure requests to https
SECURE_SSL_REDIRECT = True

# Allow all host headers
ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# set to use postgre backend in production
DATABASES['default'] = dj_database_url.parse( os.environ.get("DATABASE_URL"),
                                                 conn_max_age=600) 


# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



#======= config for AmazonS3 storage -> media files upload======
        
        # read credentials from environment variables   
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME') 

AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}

AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')    
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME



MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'wentors_site.settings.aws_file_storage.MediaStorage'



### chaching setting for performance

# default cache
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': os.environ.get('REDIS_URL'),
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#         }
#     },
#   # rendition for cacheing images
#     'renditions': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         'LOCATION':  os.environ['MEMCACHIER_SERVERS'],
#         'TIMEOUT': 600,
#         'OPTIONS': {
#             # 'MAX_ENTRIES': 1000,
#             'binary': True,
#             'username': os.environ['MEMCACHIER_USERNAME'],
#             'password': os.environ['MEMCACHIER_PASSWORD']
#         }
#     }
# }

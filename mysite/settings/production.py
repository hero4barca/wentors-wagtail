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


try:
    from .local import *
except ImportError:
    pass

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
DEFAULT_FILE_STORAGE = 'mysite.settings.aws_file_storage.MediaStorage'


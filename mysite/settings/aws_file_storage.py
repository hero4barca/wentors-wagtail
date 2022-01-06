from storages.backends.s3boto3 import S3Boto3Storage


# subclassing s3boto3Storage
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False # don't multiple file with same name 
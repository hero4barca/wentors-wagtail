

Create the following environment variables:

standard env vars for prod:
    ENV_NAME=production
    DJANGO_SECRET_KEY=[generated django secret key]
    DATABASE_URL=[database url] # for postgre db
    AWS_STORAGE_BUCKET_NAME = []

for static files storage (stored on amazon s3):
    AWS_STORAGE_BUCKET_NAME = [aws bucket name]   
    AWS_SECRET_ACCESS_KEY = [aws secret access key] 
    AWS_S3_REGION_NAME = [aws region name]
    AWS_ACCESS_KEY_ID = [asws access key id]


import boto3


s3 = boto3.client('s3')
filename = 'file.txt'
bucket_name = 'vansledright-personal-backup'

s3.upload_file(filename, bucket_name, filename)
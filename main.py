import boto3
import os
import sys

s3_resource = boto3.resource(
    's3',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2]
)
def upload_objects():
    try:
        root_path = sys.argv[3]
        bucket_name = sys.argv[4]
        my_bucket = s3_resource.Bucket(bucket_name)

        for path, subdirs, files in os.walk(root_path, followlinks=True) :
            path = path.replace("\\", "/")
            directory_name = path.replace(root_path,"")
            for file in files:
                my_bucket.upload_file(os.path.join(path, file), directory_name+'/'+file)

    except Exception as err:
        print(err)

if __name__ == '__main__':
    upload_objects()
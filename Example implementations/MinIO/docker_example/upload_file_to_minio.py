import boto3
from botocore.client import Config

# Replace these values with your own AWS credentials and bucket name
ACCESS_KEY = 'your_access_key'
SECRET_KEY = 'your_secret_key'
BUCKET_NAME = 'your_bucket_name'

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """Upload a file to S3."""
    s3_client = boto3.client('s3',
                endpoint_url='https://s3.deltares.nl',
                aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY,
                config=Config(signature_version='s3v4'),
                region_name='eu-west-1')

    if object_name is None:
        object_name = file_name

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded successfully to '{bucket_name}/{object_name}'")
    except Exception as e:
        print(f"Error uploading file '{file_name}' to S3: {e}")

def main():
    # File to upload
    file_to_upload = 'dataset.json'

    # Upload file to S3
    upload_file_to_s3(file_to_upload, BUCKET_NAME)

if __name__ == "__main__":
    main()

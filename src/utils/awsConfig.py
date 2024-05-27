import boto3
from src.config import AWSConfig
import base64

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWSConfig.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWSConfig.AWS_SECRET_ACCESS_KEY,
    region_name=AWSConfig.AWS_DEFAULT_REGION
)

def awsConfig(file_key):
    try:
        response = s3_client.get_object(Bucket=AWSConfig.S3_BUCKET_NAME, Key=file_key)
        file_data = response['Body'].read()
        return base64.b64encode(file_data).decode('utf-8')
    except Exception as e:
        print(e)
        return str(e), 500
import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CIPHER_EXTEND = os.environ.get("CIPHER_EXTEND")
    BASEURL = os.environ.get("BASEURL")
    
    JWT_SECRET = os.environ.get("JWT_SECRET")
    DATABASE_NAME = os.environ.get("DATABASE")
    FILE_CRYPT = os.environ.get("FILE_CRYPT")

class EmailConfig:
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")

class AWSConfig:
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CIPHER_EXTEND = os.environ.get("CIPHER_EXTEND")
    BASEURL = os.environ.get("BASEURL")
    
    JWT_SECRET = os.environ.get("JWT_SECRET")
    DATABASE_NAME = os.environ.get("DATABASE")

class EmailConfig:
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
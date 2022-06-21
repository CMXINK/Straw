import os
import uuid


class Config:
    DEBUG = True
    # 数据库+驱动://user:password@hostip:port/databasename
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/straw_raw_material'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = str(uuid.uuid4())  # 用于session加密的secret_key
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    compare_type = True
    """
    默认邮箱,发送者以及授权码
    """
    MAIL_SERVER = "smtp.163.com"
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True
    MAIL_POST = 25
    MAIL_USERNAME = "LJ3393370171@163.com"
    MAIL_PASSWORD = "OHIGQXSHCHDPDACR"
    MAIL_DEFAULT_SENDER = "LJ3393370171@163.com"
    # MAIL_USE_TLS = True
    # MAIL_MAX_EMAILS = 20


class DevelopmentConfig(Config):
    ENV = "development"
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False

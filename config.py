import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'yiwj\xfa\xe0\x18\xe7\xde\xa1\x8b#\x9e\xdbyXqC\x9e\xcdK\xcaz8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# development config
class DevelopmentConfig(BaseConfig):
    DEBUG = True


# development config
class ProductionConfig(BaseConfig):
    DEBUG = False

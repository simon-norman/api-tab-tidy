import os


class Config(object):
    ENV = os.environ['ENVIRONMENT']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['TAB_TIDY_DB_URL']

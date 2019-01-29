import os

class DevelopmentConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ['TAB_TIDY_DB_URL']
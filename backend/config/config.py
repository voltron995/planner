import os
basedir = os.path.abspath(os.path.dirname(__file__) + '/../../')


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    LOG = basedir + '/log/planner.log'


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL="WARN"


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOG_LEVEL = "DEBUG"


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    LOG_LEVEL = "DEBUG"


class TestingConfig(Config):
    TESTING = True
    LOG_LEVEL = "DEBUG"

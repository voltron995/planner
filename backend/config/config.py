import os
import json, logging.config
basedir = os.path.abspath(os.path.dirname(__file__) + '/../../')


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True



class ProductionConfig(Config):
    DEBUG = False
    with open(basedir + '/backend/config/prodLog.json') as f:
        conf = json.load(f)
    logging.config.dictConfig(conf)

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    with open(basedir + '/backend/config/devLog.json') as f:
        conf = json.load(f)
    logging.config.dictConfig(conf)


class TestingConfig(Config):
    TESTING = True

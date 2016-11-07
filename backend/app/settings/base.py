import os
import logging.config
from .local import *

basedir = os.path.abspath(os.path.dirname(__file__) + '/../../..')

TESTING = False
CSRF_ENABLED = True
DEVELOPMENT = True
DEBUG = True
config_dict = {
    "version": 1,
    "formatters": {
        "brief": {
            "format": "%(levelname)-8s: %(name)-15s: %(message)s"
        },
        "full": {
            "format": "%(asctime)s %(name)-15s %(levelname)-8s %(message)s"
        }
    },
    "handlers": {
        "filelog": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "full",
            "level": "INFO",
            "filename": basedir + '/log/planner.log'
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "brief",
            "level": "WARN",
            "stream": "ext://sys.stderr"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "filelog",
            "console"
        ]
    }
}

logging.config.dictConfig(config_dict)

FLASKY_MAIL_SUBJECT_PREFIX = '[Planner]'
FLASKY_MAIL_SENDER = 'Planner <planner018@yandex.ru>'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = '{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DB_CONFIG)

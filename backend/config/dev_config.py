from config.config import *
from config.local import *
import logging.config

DEVELOPMENT = True
DEBUG = True
config_dict = {
        "version": 1,
        "formatters": {
            "brief": {"format": "%(levelname)-8s: %(name)-15s: %(message)s"},
            "full": {"format": "%(asctime)s %(name)-15s %(levelname)-8s %(message)s"}
        },
        "handlers": {
            "filelog": {
                "class": "logging.handlers.RotatingFileHandler",
                "formatter": "full",
                "level": "INFO",
                "filename": basedir + '/log/planner.log'},
            "console": {
                "class":"logging.StreamHandler",
                "formatter": "brief",
                "level": "WARN",
                "stream": "ext://sys.stderr"}
        },
        "root": {"level": "DEBUG", "handlers": ["filelog", "console"]}
    }
logging.config.dictConfig(config_dict)
from .base import *

DB_CONFIG = {
    'DRIVER': 'postgresql',
    'USER': 'postgres',
    'PASSWORD': 'pass',
    'HOST': '127.0.0.1',
    'PORT': 5432,
    'NAME': 'planner_dev'
}

SQLALCHEMY_DATABASE_URI = '{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DB_CONFIG)


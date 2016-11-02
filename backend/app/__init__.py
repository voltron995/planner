import os
from flask import Flask
import config.config as config
from flask_migrate import Migrate
from .database import db


def create_app():
    app = Flask(__name__, static_url_path='/dist')

    app.config.from_pyfile('../config/' + os.environ['APP_SETTINGS'])
    migrate = Migrate(app, db)

    from . import events
    from . import users
    from . import msclient

    from app.events import models
    from app.users import models
    from app.msclient import models

    from app.events import module as events_module
    from app.users import module as users_module

    app.register_blueprint(events_module)
    app.register_blueprint(users_module)

    return app

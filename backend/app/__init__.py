import os
from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/dist')
    # app.config.from_object(os.environ['APP_SETTINGS'])

    from . import events
    from . import users

    from app.events import models
    from app.users import models

    from app.events import module as events_module
    from app.users import module as users_module

    app.register_blueprint(events_module)
    app.register_blueprint(users_module)

    return app

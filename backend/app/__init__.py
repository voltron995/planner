from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_url_path='/dist')

app.config.from_object('app.settings.base')

db = SQLAlchemy()
migrate = Migrate(app, db)

from . import events
from . import users
from . import msclient

from app.events import events as events_blueprint
from app.users import users as users_blueprint
app.register_blueprint(events_blueprint)
app.register_blueprint(users_blueprint)

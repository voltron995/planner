from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/dist')

app.config.from_object('app.settings.base')

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

Session(app)

login_manager = LoginManager()
login_manager.init_app(app)

bootstrap = Bootstrap(app)
mail = Mail(app)

from . import events
from . import users
from . import targets
from . import plugins
from . import uploads
from . import error_handlers
from . import urls

from app.users import users_blueprint

app.register_blueprint(users_blueprint)


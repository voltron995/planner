from flask import Blueprint

module = Blueprint('users', __name__, url_prefix='/users')

from . import urls
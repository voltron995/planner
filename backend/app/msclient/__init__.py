from flask import Blueprint

module = Blueprint('msclient', __name__, url_prefix='/ms')

from .api import urls
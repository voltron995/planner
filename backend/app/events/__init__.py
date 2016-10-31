from flask import Blueprint

module = Blueprint('events', __name__, url_prefix='/events', template_folder='events')

from . import urls

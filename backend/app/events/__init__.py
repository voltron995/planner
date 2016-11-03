from flask import Blueprint

events = Blueprint('events', __name__, url_prefix='/events', template_folder='events')

from . import urls
from . import models

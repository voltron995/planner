from flask import Blueprint

events_blueprint = Blueprint('items', __name__, url_prefix='/items', template_folder='items')

from . import models
from . import api

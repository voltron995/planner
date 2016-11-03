from flask import Blueprint

msclient = Blueprint('msclient', __name__, url_prefix='/ms')

from .api import urls
from . import models

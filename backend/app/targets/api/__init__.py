from app.api import Api

api_targets = Api('targets', url_prefix='/targets')

from . import urls


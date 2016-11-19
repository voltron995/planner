from app.api import Api

api_plugins = Api('plugins', url_prefix='/plugins')

from . import urls

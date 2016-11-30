from app.api import Api

api_items = Api('items', url_prefix='/items')

from . import urls


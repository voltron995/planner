from app.api import Api

api_events = Api('users', url_prefix='/users')

from . import urls

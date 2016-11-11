from app.api import Api

api_events = Api('events', url_prefix='/events')

from . import urls


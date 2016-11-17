from app.events.api import permitters
from . import api_events
from . import views, validators

api_events.add_url_rule(
    '/',
    view_func=views.EventList.as_view('list'),
    validator=validators.List,
    permitter=permitters.List
)
api_events.add_url_rule(
    '/<event_uuid>',
    view_func=views.EventSingle.as_view('single'),
    validator=validators.Single,
    permitter=permitters.Single
)


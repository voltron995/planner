from . import api_events
from . import views, validators

api_events.add_url_rule('/', view_func=views.EventList.as_view('list'), validator=validators.List)
api_events.add_url_rule('/<event_id>', view_func=views.EventSingle.as_view('single'), validator=validators.Single)


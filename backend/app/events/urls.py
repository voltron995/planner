from . import events
from . import views

events.add_url_rule('/', view_func=views.EventsList.as_view('events_list'))
events.add_url_rule('/<event_id>', view_func=views.EventsSingle.as_view('events_single'))


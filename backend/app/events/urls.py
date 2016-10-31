from . import module
from . import views

module.add_url_rule('/', view_func=views.EventsList.as_view('events_list'))
module.add_url_rule('/<event_id>', view_func=views.EventsSingle.as_view('events_single'))


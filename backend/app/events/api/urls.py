from app.api import Permitter
from app.events.api import api_events
from app.events.api import permitters
from app.events.api import views

api_events.add_url_rule(
    '/',
    view_func=views.EventList.as_view('list'),
    permitter=Permitter
)
api_events.add_url_rule(
    '/<id>',
    view_func=views.EventSingle.as_view('single'),
    permitter=permitters.EventSinglePermitter
)


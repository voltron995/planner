from app.api.views import ListCreateView, ReadUpdateDeleteView
from app.events.api.schemas import EventSchema
from app.events.models import Event


class EventList(ListCreateView):
    model = Event
    schema = EventSchema


class EventSingle(ReadUpdateDeleteView):
    model = Event
    schema = EventSchema

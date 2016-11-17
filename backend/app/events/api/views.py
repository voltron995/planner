from flask import jsonify
from flask_login import current_user
from flask.views import MethodView

from app.api import response
from app.events.api.schemas import EventSchema
from app.events.models import Event


class EventList(MethodView):
    def get(self):
        events = current_user.events
        return response.success(data=events, schema=EventSchema, many=True)


class EventSingle(MethodView):
    def get(self, event_uuid):
        event = Event.query.filter_by(uuid=event_uuid).first()
        return response.success(data=event, schema=EventSchema)

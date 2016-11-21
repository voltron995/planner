from flask import request
from flask_login import current_user
from flask.views import MethodView
from app import db

from app.api import response
from app.events.api.schemas import EventSchema
from app.events.models import Event
from app.users.models import User


def process_single_event(method_view):
    def wrapper(self, event_uuid):
        event = Event.query.filter_by(uuid=event_uuid).first()
        method_view(self, event)
        return response.success(data=event, schema=EventSchema)

    return wrapper


class EventList(MethodView):
    def get(self):
        events = current_user.events
        return response.success(data=events, schema=EventSchema, many=True)

    def post(self):
        event_attributes = request.json['data']['attributes']
        event_attributes['user'] = current_user
        event = Event(**event_attributes)
        db.session.add(event)
        db.session.commit()
        return response.success(data=event, schema=EventSchema)


class EventSingle(MethodView):
    @process_single_event
    def get(self, event):
        pass

    @process_single_event
    def put(self, event):
        event.query.update(request.json["data"]["attributes"])
        db.session.commit()

    @process_single_event
    def delete(self, event):
        db.session.delete(event)
        db.session.commit()

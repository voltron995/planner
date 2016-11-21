from flask import request
from flask_login import current_user
from flask.views import MethodView
from app import db

from app.api import response
from app.events.api.schemas import EventSchema
from app.events.models import Event
from app.users.models import User


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
    def get(self, event_uuid):
        event = Event.query.filter_by(uuid=event_uuid).first()
        return response.success(data=event, schema=EventSchema)

    def put(self, event_uuid):
        event = Event.query.filter_by(uuid=event_uuid).first()
        event.query.update(request.json["data"]["attributes"])
        db.session.commit()
        return response.success(data=event, schema=EventSchema)
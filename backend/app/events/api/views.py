from flask import request
from flask.views import MethodView
from flask_login import current_user

from app import db
from app.api import response
from app.events.api.schemas import EventSchema
from app.events.models import Event


class EventList(MethodView):
    def get(self):
        return response.success(data=current_user.events, schema=EventSchema, many=True)

    def post(self):
        data = request.json
        data['user'] = current_user

        event = Event.create(**data)
        db.session.commit()

        return response.success(data=event, schema=EventSchema)


class EventSingle(MethodView):
    def get(self, id):
        return response.success(data=Event.get_or_404(id), schema=EventSchema)

    def put(self, id):
        event = Event.get_or_404(id)
        event.update(request.json)
        db.session.commit()
        return response.success(data=event, schema=EventSchema)

    def delete(self, id):
        Event.get_or_404(id).delete()
        db.session.commit()
        return response.success()

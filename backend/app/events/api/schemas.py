from dateutil import parser
from flask import request
from marshmallow import fields, validate
from marshmallow import validates_schema

from app.api.schemas import ModelSchema
from app.errors import BadRequest, InvalidAttribute
from app.events.models import Event


class EventSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(max=64)], required=True)
    description = fields.Str()
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    is_done = fields.Boolean()
    user_id = fields.Str(required=True, dump_only=True)
    target_id = fields.Str()

    @validates_schema
    def validate_time(self, data):
        if request.view_args.get('id'):
            event = Event.query.get(request.view_args.get('id'))
            start_time = event.start_time
            end_time = event.end_time

        if 'start_time' in data:
            start_time = data['start_time']
        if 'end_time' in data:
            end_time = data['end_time']
        # todo: fix 'can't compare offset-naive and offset-aware datetimes'
        if start_time > end_time:
            raise BadRequest(InvalidAttribute(detail='Start_time cannot be later than end_time.'))

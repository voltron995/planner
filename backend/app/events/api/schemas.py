import pytz
from app.error_handlers.errors import InvalidAttribute
from flask import request
from marshmallow import fields, validate
from marshmallow import validates_schema

from app.api.schemas import ModelSchema
from app.error_handlers.exceptions import APIBadRequest
from app.events.models import Event
from app.items.api.schemas import ItemSchema


class EventSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(max=64)], required=True)
    description = fields.Str()
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    color_primary = fields.Str()
    color_secondary = fields.Str()
    is_done = fields.Boolean()
    user_id = fields.Str(required=True, dump_only=True)
    target_id = fields.Str(required=False)
    items = fields.Nested(ItemSchema, many=True, dump_only=True)

    @validates_schema
    def validate_time(self, data):
        if request.view_args.get('id'):
            event = Event.query.get(request.view_args.get('id'))
            start_time = event.start_time
            end_time = event.end_time

        if 'start_time' in data:
            start_time = self.make_datetime_aware(data['start_time'])

        if 'end_time' in data:
            end_time = self.make_datetime_aware(data['end_time'])
        if start_time > end_time:
            raise APIBadRequest(InvalidAttribute(detail='Start_time cannot be later than end_time.'))

    def make_datetime_aware(self, time):
        if not time.tzinfo:
            time = time.replace(tzinfo=pytz.UTC)
        return time

from marshmallow import fields, validate

from app.api.schemas import BaseSchema


class EventSchema(BaseSchema):
    _type = 'events'
    name = fields.Str(validate=[validate.Length(max=64)], required=True)
    description = fields.Str()
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    is_done = fields.Boolean(required=True)


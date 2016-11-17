from marshmallow import fields, validate

from app.api.schemas import BaseSchema


class EventSchema(BaseSchema):
    _type = 'events'
    name = fields.Str(validate=[validate.Length(max=64)])
    description = fields.Str()
    start_time = fields.DateTime()
    end_time = fields.DateTime()
    status = fields.Boolean()

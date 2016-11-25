from marshmallow import fields, validate

from app.api.schemas import ModelSchema


class EventSchema(ModelSchema):
    name = fields.Str(validate=[validate.Length(max=64)], required=True)
    description = fields.Str()
    start_time = fields.DateTime(required=True)
    end_time = fields.DateTime(required=True)
    is_done = fields.Boolean(required=True)
    user_id = fields.Str(required=True, dump_only=True)
    target_id = fields.Str()


from marshmallow import fields, validate

from app.api.schemas import ModelSchema


class TargetSchema(ModelSchema):
    name = fields.Str(required=True, validate=[validate.Length(max=255)])
    is_done = fields.Boolean(required=True)
    user_id = fields.Str(required=True, dump_only=True)
    target_id = fields.Str()


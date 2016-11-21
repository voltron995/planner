from marshmallow import fields, validate

from app.api.schemas import BaseSchema


class TargetSchema(BaseSchema):
    _type = 'targets'

    id = fields.Integer()
    name = fields.Str(required=True, validate=[validate.Length(max=255)])
    is_done = fields.Boolean(required=True, load_only=True)
    user_id = fields.Integer(required=True, dump_only=True)
    target_id = fields.Integer()


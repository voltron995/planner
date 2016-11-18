from marshmallow import fields, validate

from app.api.schemas import BaseSchema

choises = ['achieved', 'in_progress', 'failed']


class TargetSchema(BaseSchema):
    _type = 'targets'

    id = fields.Integer()
    name = fields.Str(validate=[validate.Length(max=255)])
    status = fields.Str(required=True, validate=[validate.OneOf(choices=choises)], load_only=True)
    user_id = fields.Integer()
    target_id = fields.Integer()


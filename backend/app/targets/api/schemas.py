from app.error_handlers.errors import InvalidAttribute
from flask_login import current_user
from marshmallow import fields, validate
from marshmallow import validates

from app.api.schemas import ModelSchema
from app.error_handlers.exceptions import APIBadRequest


class TargetSchema(ModelSchema):
    name = fields.Str(required=True, validate=[validate.Length(max=255)])
    is_done = fields.Boolean()
    user_id = fields.Str(required=True, dump_only=True)
    target_id = fields.Str()
    description = fields.Str()

    @validates('target_id')
    def validate_target_id(self, target_id):
        # todo: rewrite
        target_ids = {target.id for target in current_user.targets}
        if target_id not in target_ids:
            raise APIBadRequest(InvalidAttribute('Wrong data'))

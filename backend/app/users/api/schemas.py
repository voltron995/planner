from flask_login import current_user
from marshmallow import fields, validate

from app.api.schemas import BaseSchema
from app.errors import BadRequest, InvalidAttribute
from app.uploads.uploads_manager import UploadsManager


# todo: move this function somewhere?
def is_temp_image_exists(image_uuid: str):
    if image_uuid and image_uuid != current_user.profile.image:
        if not UploadsManager.is_tmp_file(image_uuid):
            raise BadRequest(InvalidAttribute('Uploaded image not found'))


class ProfileSchema(BaseSchema):
    _type = 'profiles'

    first_name = fields.Str(validate=[validate.Length(max=64)], allow_none=True)
    last_name = fields.Str(validate=[validate.Length(max=64)], allow_none=True)
    birth_date = fields.Date(allow_none=True)
    image = fields.Str(validate=[validate.Length(max=64), is_temp_image_exists], allow_none=True)
    image_link = fields.Str(validate=[validate.Length(max=64)], dump_only=True)


class UserSchema(BaseSchema):
    _type = 'users'

    login = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    last_access = fields.DateTime(dump_only=True)
    profile = fields.Nested(ProfileSchema, dump_only=True)
    password = fields.Str(required=True, validate=[validate.Length(min=6, max=64)], load_only=True)
    confirm = fields.Str(required=True, validate=[validate.Length(min=6, max=64)], load_only=True)

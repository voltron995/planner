from flask_login import current_user
from marshmallow import fields, validate
from marshmallow import validates
from marshmallow import validates_schema

from app.api.schemas import ModelSchema
from app.error_handlers.errors import InvalidAttribute
from app.error_handlers.exceptions import APIBadRequest
from app.uploads.manager import UploadsManager


class ProfileSchema(ModelSchema):
    first_name = fields.Str(validate=[validate.Length(max=64)], allow_none=True)
    last_name = fields.Str(validate=[validate.Length(max=64)], allow_none=True)
    birth_date = fields.Date(allow_none=True)
    image = fields.Str(validate=[validate.Length(max=64)], allow_none=True)
    image_link = fields.Str(validate=[validate.Length(max=64)], dump_only=True)

    @validates('image')
    def is_tmp_image_exists(self, image_id):
        if image_id and image_id != current_user.profile.image:
            if not UploadsManager.is_tmp_file(image_id):
                raise APIBadRequest(InvalidAttribute(detail='Uploaded image not found'))


class UserSchema(ModelSchema):
    login = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    last_access = fields.DateTime(dump_only=True)
    profile = fields.Nested(ProfileSchema, dump_only=True)
    old_password = fields.Str(required=True, load_only=True)
    password = fields.Str(required=True, validate=[validate.Length(min=6, max=64)], load_only=True)
    confirm = fields.Str(required=True, validate=[validate.Length(min=6, max=64)], load_only=True)

    @validates_schema
    def validate_password_confirmation(self, data):

        old_password = data.get('old_password')
        if old_password:
            self._validate_old_password(old_password)

        password = data.get('password')
        confirm = data.get('confirm')
        if password and confirm:
            self._validate_password_confirmation(password, confirm)

    def _validate_old_password(self, old_password):
        if not current_user.verify_password(old_password):
            raise APIBadRequest(InvalidAttribute(detail='Password confirmation failed.'))

    def _validate_password_confirmation(self, password, confirm):
        if password != confirm:
            raise APIBadRequest(InvalidAttribute(detail='Password confirmation mismatch.'))
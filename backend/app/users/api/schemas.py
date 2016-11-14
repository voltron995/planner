from marshmallow import fields, validate

from app.api.schemas import BaseSchema


class ProfileSchema(BaseSchema):
    _type = 'profiles'

    first_name = fields.Str(validate=[validate.Length(max=64)])
    last_name = fields.Str(validate=[validate.Length(max=64)])
    birth_date = fields.Date()
    image_path = fields.Str()


class UserSchema(BaseSchema):
    _type = 'users'

    login = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    last_access = fields.DateTime(dump_only=True)
    profile = fields.Nested(ProfileSchema, dump_only=True)
    password = fields.Str(required=True, validate=[validate.Length(min=6, max=64)], load_only=True)
    confirm = fields.Str(required=True, validate=[validate.Length(min=6, max=64)], load_only=True)

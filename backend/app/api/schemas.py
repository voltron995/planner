from marshmallow import Schema, fields, validate, pre_load, post_dump

from app.errors import BadRequest
from app.errors import Error


class BaseSchema(Schema):
    _type = ''

    uuid = fields.Str(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many):
        return {
            'uuid': data.pop('uuid', None),
            'type': self._type,
            'attributes': data
        }

    @pre_load
    def process_input(self, json_input):
        if 'data' not in json_input:
            raise BadRequest(Error('Required DATA member is missing.'))

        data = json_input['data']
        if self._type != data['type']:
            raise BadRequest(Error('Invalid schema type.'))

        if 'uuid' not in data:
            raise BadRequest(Error('Required UUID member is missing.'))

        if 'attributes' not in data:
            raise BadRequest(Error('Required UUID member is missing.'))

        output = data['attributes']

        return output


class ErrorSchema(Schema):
    title = fields.Str(dump_only=True)
    detail = fields.Str(dump_only=True)
    status = fields.Int(dump_only=True)
    source = fields.Str(dump_only=True)


class ExceptionSchema(Schema):
    errors = fields.Nested(ErrorSchema, many=True, dump_only=True)


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

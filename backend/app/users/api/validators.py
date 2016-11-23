from flask_login import current_user

from app.api.validators import Validator
from app.errors import InvalidAttribute, BadRequest
from app.users.api.schemas import ProfileSchema, UserSchema


class UserCurrent(Validator):
    def put(self):
        self.validate_schema(UserSchema)

        if self._json['data']['uuid'] != current_user.uuid:
            raise BadRequest(InvalidAttribute('Invalid user uuid.'))

        attrs = self._json['data']['attributes']
        if attrs.get('password') != attrs.get('confirm'):
            raise BadRequest(InvalidAttribute('Password and confirmation mismatch.'))


class ProfileCurrent(Validator):
    def put(self):
        self.validate_schema(ProfileSchema)

        if self._json['data']['uuid'] != current_user.profile.uuid:
            raise BadRequest(InvalidAttribute('Invalid profiles uuid.'))

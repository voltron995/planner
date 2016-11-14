from app.api.validators import Validator
from app.errors import InvalidAttribute, BadRequest
from app.users.api.schemas import ProfileSchema, UserSchema


class UserSingle(Validator):
    def put(self):
        self.validate_schema(UserSchema)
        self.validate_uuid('user_uuid')

        if self._json['data']['attributes']['password'] != self._json['data']['attributes']['confirm']:
            raise BadRequest(InvalidAttribute('Password and confirmation mismatch.'))


class ProfileSingle(Validator):
    def put(self):
        self.validate_schema(ProfileSchema)
        self.validate_uuid('profile_uuid')
        # todo: validate image path

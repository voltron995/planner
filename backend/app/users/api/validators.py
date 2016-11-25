from app.api.validators import Validator
from app.users.api.schemas import ProfileSchema, UserSchema


class UserCurrent(Validator):
    def put(self):
        self.validate_schema(UserSchema)


class ProfileCurrent(Validator):
    def put(self):
        self.validate_schema(ProfileSchema)

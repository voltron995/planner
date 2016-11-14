from app.api.validators import Validator, ValidationError
from app.errors import InvalidAttribute, DefaultException
from app.users.api.schemas import ProfileSchema, UserSchema
from app.users.models import User


class UserSingle(Validator):
    def put(self):
        self.validate_schema(UserSchema)

        if self._request.view_args['user_uuid'] != self._json['data']['uuid']:
            raise ValidationError('Profile uuid in url and profile uuid in json input mismatch.')

        # current_user = User.query.all()[3]
        # if current_user.uuid != json_input['data']['uuid']:
        #     raise ValidationError('This is not your user')
        #
        # if json_input['data']['attributes']['password'] != json_input['data']['attributes']['confirm']:
        #     raise ValidationError('Passwords mismatch.')

    def get(self):
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7')
        pass


class ProfileSingle(Validator):
    def put(self):
        json_input = self._request.get_json()
        errors = ProfileSchema().validate(json_input)
        if errors:
            raise ValidationError('bad request')

        if self._request.view_args['profile_uuid'] != json_input['data']['uuid']:
            raise ValidationError('Profile uuid in url and profile uuid in json input mismatch.')

        current_user = User.query.all()[3]
        if current_user.profile.uuid != json_input['data']['uuid']:
            raise ValidationError('This is not your profile')

            # todo check image path

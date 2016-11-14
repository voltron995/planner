from flask_login import current_user

from app.api import Permitter
from app.errors import Forbidden, AccessDenied


class UserSingle(Permitter):
    def put(self):
        if current_user.uuid != self._request.view_args['user_uuid']:
            raise Forbidden(AccessDenied())


class ProfileSingle(Permitter):
    def put(self):
        if current_user.profile.uuid != self._request.view_args['profile_uuid']:
            raise Forbidden(AccessDenied())

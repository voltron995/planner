from flask import request
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user

from app import db
from app.api import response
from app.api.views import BaseView
from app.uploads import groups
from app.uploads.manager import UploadsManager
from app.users.api.schemas import UserSchema, ProfileSchema
from app.users.models import User, Profile


class UserCurrent(BaseView):
    model = User
    schema = UserSchema

    def get(self):
        return response.success(data=current_user, schema=self.schema)

    def put(self):
        self._validate_schema()

        current_user.update({'password': request.json.get('password')})
        db.session.commit()
        return response.success(data=current_user, schema=self.schema)


class ProfileCurrent(BaseView):
    model = Profile
    schema = ProfileSchema

    def put(self):
        self._validate_schema()

        data = request.json
        profile = current_user.profile

        if 'image' in data and data['image'] != profile.image:
            image_uuid = data['image']
            image = UploadsManager.get_tmp_file(image_uuid)
            UploadsManager.move_file(image, groups.PROFILE_IMAGES)

        profile.update(data)
        db.session.commit()

        return response.success(data=profile, schema=self.schema)


class UsersLogout(BaseView):
    def post(self):
        logout_user()
        return response.success()

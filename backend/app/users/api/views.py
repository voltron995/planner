from flask import request
from flask_login import current_user
from flask.views import MethodView

from app import db
from app.api import response
from app.uploads.uploads_manager import UploadsManager
from app.users.api.schemas import UserSchema, ProfileSchema


class UserCurrent(MethodView):
    def get(self):
        return response.success(data=current_user, schema=UserSchema)

    def put(self):
        user = current_user
        attrs = request.json['data']['attributes']

        user.password = attrs.get('password')
        db.session.add(user)
        db.session.commit()
        return response.success(data=user, schema=UserSchema)


class ProfileCurrent(MethodView):
    def put(self):
        profile = current_user.profile
        attrs = request.json['data']['attributes']

        if 'image' in attrs and attrs['image'] != profile.image:
            image_uuid = attrs['image']
            image = UploadsManager.get_tmp_file(image_uuid)
            UploadsManager.move_file(image, 'profile_images')

        profile.query.update(attrs)
        db.session.commit()

        return response.success(data=profile, schema=ProfileSchema)

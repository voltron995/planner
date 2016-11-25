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
        current_user.password = request.json.get('password')
        db.session.add(current_user)
        db.session.commit()
        return response.success(data=current_user, schema=UserSchema)


class ProfileCurrent(MethodView):
    def put(self):
        data = request.json
        profile = current_user.profile

        if 'image' in data and data['image'] != profile.image:
            image_uuid = data['image']
            image = UploadsManager.get_tmp_file(image_uuid)
            UploadsManager.move_file(image, 'profile_images')

        profile.query.update(data)
        db.session.commit()

        return response.success(data=profile, schema=ProfileSchema)

from flask import jsonify, request
from flask.views import MethodView

from app import db
from app.api import response
from app.errors import InvalidAttribute, AccessDenied
from app.users.api.schemas import UserSchema, ProfileSchema
from app.users.models import User, Profile


class UserSingle(MethodView):
    def get(self, user_uuid):
        user = User.query.filter_by(login='masha').first()
        return response.success(data=user, schema=UserSchema)

    def put(self, user_uuid):
        user = User.query.filter_by(login='masha').first()
        user.password = request.json['data']['attributes']['password']
        db.session.commit()
        return response.success(data=user, schema=UserSchema)


class ProfileSingle(MethodView):
    def put(self, profile_uuid):
        profile = Profile.query.get(1)
        profile.query.update(request.json['data']['attributes'])
        db.session.commit()

        return response.success(data=profile, schema=ProfileSchema)


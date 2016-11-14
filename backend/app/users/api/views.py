from flask import jsonify, request
from flask.views import MethodView

from app import db
from app.users.api.schemas import UserSchema, ProfileSchema
from app.users.models import User, Profile


class UserSingle(MethodView):
    def get(self, user_uuid):
        user = User.query.filter_by(login='masha').first()
        data, _ = UserSchema().dump(user)
        return jsonify(data=data)

    def put(self, user_uuid):
        user = User.query.filter_by(login='masha').first()
        user.password = request.json['data']['attributes']['password']
        db.session.commit()
        data, _ = UserSchema().dump(user)
        return jsonify(data=data)


class ProfileSingle(MethodView):
    def put(self, profile_uuid):
        profile = Profile.query.get(1)
        profile.query.update(request.json['data']['attributes'])
        db.session.commit()

        data, _ = ProfileSchema().dump(profile)
        return jsonify(data=data)

from flask_login import current_user
from flask.views import MethodView
from flask import request
from app.api import response
from app import db
import json
from app.targets.api.schemas import TargetSchema
from app.targets.models import Target
from app.users.models import User

OK = json.dumps({"OK": 200})


class TargetsList(MethodView):

    def get(self):
        current_user = User.query.first()
        targets = current_user.targets
        return response.success(data=targets, schema=TargetSchema, many=True)

    def post(self):
        current_user = User.query.first()
        target_data = request.json.get("data").get("attributes")
        target_data['user_id'] = current_user.id
        new_target = Target(**target_data)

        db.session.add(new_target)
        db.session.commit()
        return response.success(data=new_target, schema=TargetSchema)


class TargetSingle(MethodView):
    def get(self, target_uuid):
        target_data = Target.query.filter_by(uuid=target_uuid).first()
        return response.success(data=target_data, schema=TargetSchema)

    def put(self, target_uuid):
        target_data = Target.query.filter_by(uuid=target_uuid).first()
        target_data.query.update(request.json["data"]["attributes"])

        db.session.commit()
        return response.success(data=target_data, schema=TargetSchema)

    def delete(self, target_uuid):
        target_to_delete = Target.query.filter_by(uuid=target_uuid).first()
        db.session.delete(target_to_delete)
        db.session.commit()
        return OK

from flask_login import current_user
from flask.views import MethodView
from flask import request
from app.api import response
from app import db
from app.targets.api.schemas import TargetSchema
from app.targets.models import Target


class TargetsList(MethodView):
    def get(self):
        targets = current_user.targets
        return response.success(data=targets, schema=TargetSchema, many=True)


class TargetSingle(MethodView):
    def get(self, target_uuid):
        target_data = Target.query.filter_by(uuid=target_uuid).first()
        return response.success(data=target_data, schema=TargetSchema)

    def put(self, target_uuid):
        new_target_data = request.json
        target_data = Target.query.filter_by(uuid=target_uuid).first()
        target_data.name = new_target_data.get("name") or target_data.name
        target_data.is_done = new_target_data.get("is_done") or target_data.is_done
        db.session.commit()
        return response.success(data=target_data, schema=TargetSchema)

    def post(self):
        target = request.json
        target_data = Target(
                        name=target.get('name'),
                        is_done=target.get("is_done")
                        )
        db.session.add(target_data)
        db.session.commit()
        return response.success(data=target_data, schema=TargetSchema)

    def delete(self, target_uuid):
        target_to_delete = Target.query.filter_by(uuid=target_uuid).first()
        db.session.delete(target_to_delete)
        db.session.commit()


from flask import jsonify
from flask_login import current_user
from flask.views import MethodView

from app.api import response
from app.targets.api.schemas import TargetSchema
from app.targets.models import Target


class TargetsList(MethodView):
    def get(self):
        targets = current_user.events
        return response.success(data=targets, schema=TargetSchema, many=True)


class TargetSingle(MethodView):
    def get(self, target_uuid):
        target_data = Target.query.filter_by(uuid=target_uuid).first()
        return response.success(data=target_data, schema=TargetSchema)

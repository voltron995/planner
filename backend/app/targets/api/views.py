from flask import request
from flask.views import MethodView
from flask_login import current_user

from app import db
from app.api import response
from app.targets.api.schemas import TargetSchema
from app.targets.models import Target


class TargetsList(MethodView):

    def get(self):
        return response.success(data=current_user.targets, schema=TargetSchema, many=True)

    def post(self):
        data = request.json
        data['user_id'] = current_user.id

        target = Target(**data)
        db.session.add(target)
        db.session.commit()

        return response.success(data=target, schema=TargetSchema)


class TargetSingle(MethodView):
    def get(self, id):
        return response.success(data=Target.query.get(id), schema=TargetSchema)

    def put(self, id):
        target = Target.query.get(id)
        target.query.update(request.json)
        db.session.commit()
        return response.success(data=target, schema=TargetSchema)

    def delete(self, id):
        target = Target.query.get(id)
        db.session.delete(target)
        db.session.commit()
        return response.success()

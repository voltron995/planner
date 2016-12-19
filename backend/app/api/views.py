from app.error_handlers.errors import Error
from flask import request
from flask.ext.login import current_user
from flask.views import MethodView

from app import db
from app.api import response
from app.api.schemas import ModelSchema
from app.error_handlers.exceptions import APIBadRequest
from app.models import BaseModel


class BaseView(MethodView):
    model = None  # type: BaseModel
    schema = None  # type: ModelSchema

    def _validate_schema(self, partial=None):
        try:
            json = request.get_json()
        except Exception as e:
            raise APIBadRequest(Error(title='JSON decode exception.', detail=str(e)))
        self.schema().validate(json, partial=partial)


class ReadUpdateDeleteView(BaseView):
    methods = ['GET', 'PUT', 'DELETE']

    def get(self, id):
        return response.success(data=self.model.get_or_404(id), schema=self.schema)

    def put(self, id):
        self._validate_schema(partial=True)

        instance = self.model.get_or_404(id)
        instance.update(request.json)
        db.session.commit()
        return response.success(data=instance, schema=self.schema)

    def delete(self, id):
        self.model.get_or_404(id).delete()
        db.session.commit()
        return response.success()


class ListCreateView(BaseView):
    methods = ['GET', 'POST']

    def get(self):
        data = self.model.filter_by(user_id=current_user.id)
        return response.success(data=data, schema=self.schema, many=True)

    def post(self):
        self._validate_schema()

        data = request.json
        data['user_id'] = current_user.id

        instance = self.model.create(**data)
        db.session.commit()

        return response.success(data=instance, schema=self.schema)

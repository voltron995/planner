from flask import request
from flask.ext.login import current_user
from flask.views import MethodView

from app import db
from app.api import response
from app.api.schemas import ModelSchema
from app.errors import BadRequest, InvalidAttribute, Error
from app.models import BaseModel


class BaseView(MethodView):
    model = None  # type: BaseModel
    schema = None  # type: ModelSchema

    def _validate_schema(self, partial=None):
        """
        :param bool|tuple partial: Whether to ignore missing fields. If its value is an iterable,
            only missing fields listed in that iterable will be ignored.
        """
        errors = self.schema().validate(self.__parse_json(), partial=partial)
        if errors:
            exception = BadRequest()
            for attr, messages in errors.items():
                for msg in messages:
                    exception.add_error(InvalidAttribute(source=attr, detail=msg))
            raise exception

    def __parse_json(self):
        if request.is_json:
            try:
                return request.get_json()
            except Exception as e:
                raise BadRequest(Error(title='JSON decode exception.', detail=str(e)))
        else:
            return {}


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

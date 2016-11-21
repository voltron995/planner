from app.api.validators import Validator
from app.errors import InvalidAttribute, BadRequest
from app.targets.api.schemas import TargetSchema


class TargetSingle(Validator):
    def put(self):
        self.validate_schema(TargetSchema)
        self.validate_uuid('target_uuid')

        if self._json['data']['attributes'] != self._json['data']['attributes']:
            raise BadRequest(InvalidAttribute('Wrong data'))


class TargetsList(Validator):
    def post(self):
        pass

    def get(self):
        pass

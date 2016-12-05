from app.error_handlers.errors import InvalidAttribute
from flask_login import current_user

from app.api.validators import Validator
from app.error_handlers.exceptions import APIBadRequest
from app.targets.api.schemas import TargetSchema


class TargetSingle(Validator):

    def put(self):
        self.validate_schema(TargetSchema, partial=True)
        self.validate_uuid('target_uuid')

        if "target_id" in self._json['data']['attributes']:
            targets = current_user.targets
            target_ids = {target.id for target in targets}
            if self._json['data']['attributes']["target_id"] not in target_ids:
                raise APIBadRequest(InvalidAttribute('Wrong data'))


class TargetsList(Validator):

    def post(self):
        self.validate_schema(TargetSchema)

        if "target_id" in self._json['data']['attributes']:
            targets = current_user.targets
            target_ids = {target.id for target in targets}
            if self._json['data']['attributes']["target_id"] not in target_ids:
                raise APIBadRequest(InvalidAttribute('Wrong data'))


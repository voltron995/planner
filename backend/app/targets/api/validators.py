from app.api.validators import Validator
from app.targets.api.schemas import TargetSchema


class TargetSingle(Validator):
    def put(self):
        self.validate_schema(TargetSchema, partial=True)


class TargetsList(Validator):
    def post(self):
        self.validate_schema(TargetSchema)

from app.api.validators import Validator
from app.events.api.schemas import EventSchema


class EventListValidator(Validator):
    def post(self):
        self.validate_schema(EventSchema)


class EventSingleValidator(Validator):
    def put(self):
        self.validate_schema(EventSchema, partial=True)


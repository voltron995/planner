from dateutil import parser

from app.api.validators import Validator
from app.errors import BadRequest, InvalidAttribute
from app.events.api.schemas import EventSchema

class EventValidator(Validator):
    def validate_date(self):
        data = self._json['data']['attributes']
        if data['start_time'] and data['end_time']:
            start_time = parser.parse(data['start_time'])
            end_time = parser.parse(data['end_time'])
            if start_time > end_time:
                raise BadRequest(InvalidAttribute(detail='Start_time cannot be later than end_time.'))

class EventListValidator(EventValidator):
    def post(self):
        self.validate_schema(EventSchema)
        self.validate_date()

    def get(self):
        pass


class EventSingleValidator(EventValidator):
    def put(self):
        self.validate_schema(EventSchema, partial=True)
        self.validate_date()

    def get(self):
        pass

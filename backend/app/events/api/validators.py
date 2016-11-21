from dateutil import parser

from app.api.validators import Validator
from app.errors import BadRequest, InvalidAttribute
from app.events.api.schemas import EventSchema
from app.events.models import Event


def validate_date_decorator(validate_date):
    def wrapper(self):
        attributes = self._json['data']['attributes']
        start_time, end_time = validate_date(self, attributes)
        if start_time > end_time:
            raise BadRequest(InvalidAttribute(detail='Start_time cannot be later than end_time.'))

    return wrapper


class EventListValidator(Validator):
    def post(self):
        self.validate_schema(EventSchema)
        self.validate_date()

    def get(self):
        pass

    @validate_date_decorator
    def validate_date(self, attributes):
        return attributes['start_time'], attributes['end_time']


class EventSingleValidator(Validator):
    def put(self):
        self.validate_schema(EventSchema, partial=True)
        self.validate_date()

    def get(self):
        pass

    @validate_date_decorator
    def validate_date(self, attributes):
        event = Event.query.filter_by(uuid=self._json['data']['uuid']).first()
        if 'start_time' in attributes:
            start_time = parser.parse(attributes['start_time'])
        else:
            start_time = event.start_time

        if 'end_time' in attributes:
            end_time = parser.parse(attributes['end_time'])
        else:
            end_time = event.end_time
        return start_time, end_time

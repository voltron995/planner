from flask_login import current_user

from app.api import Permitter
from app.errors import NotFound, Forbidden, AccessDenied, ElementNotFound
from app.events.models import Event


class EventSinglePermitter(Permitter):
    def any_method(self):
        event = Event.query.filter_by(uuid=self._request.view_args['event_uuid']).first()
        if not event:
            raise NotFound(ElementNotFound(detail='Event with this uuid cannot be found'))
        if event.user_id != current_user.id:
            raise Forbidden(AccessDenied())

    def get(self):
        self.any_method()

    def put(self):
        self.any_method()

    def delete(self):
        self.any_method()

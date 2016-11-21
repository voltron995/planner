from flask_login import current_user

from app.api import Permitter
from app.errors import NotFound, Forbidden, AccessDenied, ElementNotFound
from app.events.models import Event


class List(Permitter):
    def get(self):
        print('get list of events permitter')

    def post(self):
        print('post an event permitter')


class Single(Permitter):
    def get(self):
        event = Event.query.filter_by(uuid=self._request.view_args['event_uuid']).first()
        if not event:
            raise NotFound(ElementNotFound(detail='Event with this uuid cannot be found'))
        if event.user_id != current_user.id:
            raise Forbidden(AccessDenied())

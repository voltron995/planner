from flask_login import current_user

from app.api import Permitter
from app.errors import NotFound, Forbidden, AccessDenied, ElementNotFound
from app.targets.models import Target


class List(Permitter):
    def get(self):
        print('list of events permitter')


class Single(Permitter):
    def get(self):
        event = Target.query.filter_by(uuid=self._request.view_args['event_uuid']).first()
        if not event:
            raise NotFound(ElementNotFound(detail='Event with this uuid cannot be found'))
        if event.user_id != current_user.id:
            raise Forbidden(AccessDenied())

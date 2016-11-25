from flask_login import current_user

from app.api import Permitter
from app.errors import Forbidden, AccessDenied
from app.events.models import Event


class EventSinglePermitter(Permitter):
    def check_if_users_event(self):
        event = Event.get_or_404(self._request.view_args.get('id'))
        if event.user_id != current_user.id:
            raise Forbidden(AccessDenied())

    def get(self):
        self.check_if_users_event()

    def put(self):
        self.check_if_users_event()

    def delete(self):
        self.check_if_users_event()

from app.error_handlers.errors import AccessDenied
from flask_login import current_user

from app.api import Permitter
from app.error_handlers.exceptions import APIForbidden
from app.events.models import Event


class EventSinglePermitter(Permitter):
    def check_if_users_event(self):
        event = Event.get_or_404(self._request.view_args.get('id'))
        if event.user_id != current_user.id:
            raise APIForbidden(AccessDenied())

    def get(self):
        self.check_if_users_event()

    def put(self):
        self.check_if_users_event()

    def delete(self):
        self.check_if_users_event()

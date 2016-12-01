from flask import request
from flask_login import current_user

from app.api import Permitter
from app.errors import Forbidden, NotFound
from app.events.models import Event
from app.items.models import Item


class DishesListPermitter(Permitter):
    def post(self):
        # todo: using not validated json.
        event_id = request.json.get('event_id')
        if event_id:
            event = Event.get_or_404(event_id)
            if event.user_id != current_user.id:
                raise Forbidden()


class DishesSinglePermitter(Permitter):
    def get(self):
        self._is_users_event()

    def put(self):
        self._is_users_event()

    def delete(self):
        self._is_users_event()

    def _is_users_event(self):
        item = Item.get_by(plugin_item_id=request.view_args['id'])
        if not item:
            raise NotFound()
        if item.event.user_id != current_user.id:
            raise Forbidden()

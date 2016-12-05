from app.error_handlers.errors import AccessDenied
from flask_login import current_user

from app.api import Permitter
from app.error_handlers.exceptions import APIForbidden
from app.targets.models import Target


class List(Permitter):
    def get(self):
        print('Basic permissions')

    def post(self):
        print('Basic permissions')


class Single(Permitter):
    def check_if_users_target(self):
        target = Target.get_or_404(self._request.view_args.get('id'))
        if target.user_id != current_user.id:
            raise APIForbidden(AccessDenied())

    def get(self):
        self.check_if_users_target()

    def put(self):
        self.check_if_users_target()

    def delete(self):
        self.check_if_users_target()

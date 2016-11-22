from flask_login import current_user

from app.api import Permitter
from app.errors import NotFound, Forbidden, AccessDenied, ElementNotFound
from app.targets.models import Target


class List(Permitter):
    def get(self):
        print('Basic permissions')

    def post(self):
        print('Basic permissions')


class Single(Permitter):

    def check_if_users_target(self):
        target = Target.query.filter_by(uuid=self._request.view_args['target_uuid']).first()
        if not target:
            raise NotFound(ElementNotFound(detail='Target with this uuid cannot be found'))
        if target.user_id != current_user.id:  # current_user.id should be here
            raise Forbidden(AccessDenied())

    def get(self):
        self.check_if_users_target()

    def put(self):
        self.check_if_users_target()

    def delete(self):
        self.check_if_users_target()


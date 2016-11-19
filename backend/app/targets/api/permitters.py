from flask_login import current_user

from app.api import Permitter
from app.errors import NotFound, Forbidden, AccessDenied, ElementNotFound
from app.targets.models import Target


class List(Permitter):
    def get(self):
        print('list of targets permitter')


class Single(Permitter):
    def get(self):
        target = Target.query.filter_by(uuid=self._request.view_args['target_uuid']).first()
        if not target:
            raise NotFound(ElementNotFound(detail='Target with this uuid cannot be found'))
        if target.user_id != current_user.id:
            raise Forbidden(AccessDenied())

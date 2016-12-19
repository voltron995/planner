from app.error_handlers.errors import AccessDenied
from flask import request
from flask_login import current_user

from app.error_handlers.exceptions import APIForbidden


def permission_callback():
    try:
        permitter = PermitterFactory.get_permitter(request.endpoint)
        permitter = permitter(request)
    except KeyError as err:
        # todo: log
        print('Permitter is not registered for ', err)
    else:
        permitter.general()
        try:
            method = request.method.lower()
            permitter_func = getattr(permitter, method)
        except AttributeError as err:
            # todo: log
            print('Permitter has no method ', err)
        else:
            permitter_func()


class Permitter:
    def __init__(self, req: request):
        self._request = req

    def general(self):
        self.permit_authenticated_user()
        self.permit_active_user()

    def permit_authenticated_user(self):
        if not current_user.is_authenticated:
            raise APIForbidden(AccessDenied())

    def permit_active_user(self):
        if not current_user.is_active:
            raise APIForbidden(AccessDenied())


class PermitterFactory:
    _permitters = {}

    @classmethod
    def get_permitter(cls, endpoint: str) -> Permitter.__class__:
        return cls._permitters[endpoint]

    @classmethod
    def register_permitter(cls, endpoint: str, permitter: Permitter) -> None:
        # todo: exceptions
        cls._permitters[endpoint] = permitter

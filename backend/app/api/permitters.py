from flask import request


def permission_callback():
    try:
        permitter = PermitterFactory.get_permitter(request.endpoint)(request)
        permitter_func = getattr(permitter, request.method.lower())
    except KeyError as err:
        print('Permitter is not registered for ', err)
    except NameError as err:
        print('Permitter has no method ', err)
    else:
        permitter.general()
        permitter_func()


class Permitter:
    def __init__(self, req: request):
        self._request = req

    def general(self):
        # todo: CSRF token
        return True


class PermitterFactory:
    _permitters = {}

    @classmethod
    def get_permitter(cls, endpoint: str) -> Permitter:
        return cls._permitters[endpoint]

    @classmethod
    def register_permitter(cls, endpoint: str, permitter: Permitter) -> None:
        # todo: exceptions
        cls._permitters[endpoint] = permitter

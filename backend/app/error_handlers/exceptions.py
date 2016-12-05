from app.error_handlers.errors import Error, AccessDenied


class APIException(Exception):
    status = 503
    errors = []

    def __init__(self, *errors, status=None):
        super().__init__()
        self.errors = list(errors)
        if status is not None:
            self.status = status

    def add_error(self, error: Error):
        self.errors.append(error)


class APIForbidden(APIException):
    status = 403


class APIBadRequest(APIException):
    status = 400


class APINotFound(APIException):
    status = 404


APIExceptions = {400: APIBadRequest, 403: APIForbidden, 404: APINotFound}

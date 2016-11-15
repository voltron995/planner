from app import app
from app.api import response
from app.errors import Error, DefaultException


@app.errorhandler(Exception)
def handle_invalid_usage(exception):
    if not issubclass(exception.__class__, DefaultException):
        error = Error(detail=str(exception))
        exception = DefaultException()
        exception.add_error(error)

    return response.error(exception.status, *exception.errors)

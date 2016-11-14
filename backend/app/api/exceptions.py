from flask import jsonify

from app import app
from app.api.schemas import ExceptionSchema
from app.errors import Error, DefaultException


@app.errorhandler(Exception)
def handle_invalid_usage(exception):
    if not issubclass(exception.__class__, DefaultException):
        error = Error(detail=str(exception))
        exception = DefaultException()
        exception.add_error(error)

    data, _ = ExceptionSchema().dump(exception)
    response = jsonify(data)
    response.status_code = exception.status

    return response

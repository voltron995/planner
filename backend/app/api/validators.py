from flask import request, jsonify
from werkzeug.exceptions import BadRequest

from app import app
from app.api.exceptions import ValidationError
from app.api.schemas import ExceptionSchema, BaseSchema
from app.errors import DefaultException, Error, InvalidAttribute


def validation_callback():
    try:
        validator = ValidatorFactory.get_validator(request.endpoint)(request)
        validate_func = getattr(validator, request.method.lower())
    except KeyError as err:
        print('Validator is not registered for ', err)
    except NameError as err:
        print('Validator has no method ', err)
    else:
        validator.validate()
        validate_func()


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


class Validator:
    def __init__(self, req: request) -> None:
        self._request = req
        self._json = self._parse_json()

    def validate(self):
        print('common is good')
        return True

    def _parse_json(self):
        try:
            return self._request.get_json()
        except Exception as e:
            raise DefaultException(status=400).add_error(Error(status=400))

    def validate_schema(self, schema: BaseSchema):
        errors = schema().validate(self._json)
        if errors:
            exception = DefaultException(status=400)
            for attr, messages in errors.items():
                for msg in messages:
                    exception.add_error(InvalidAttribute(source=attr, detail=msg))
            raise exception


class ValidatorFactory:
    _validators = {}

    @classmethod
    def get_validator(cls, endpoint: str) -> Validator:
        # todo: exceptions
        return cls._validators[endpoint]

    @classmethod
    def register_validator(cls, endpoint: str, validator: Validator) -> None:
        # todo: exceptions
        cls._validators[endpoint] = validator

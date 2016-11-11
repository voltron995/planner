from flask import request, jsonify

from app import app
from app.api.exceptions import ValidationError


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


@app.errorhandler(ValidationError)
@app.errorhandler(Exception)
def handle_invalid_usage(error):
    if issubclass(error.__class__, ValidationError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
    else:
        response = jsonify({'status_code': 413, 'message': 'polomalos'})
        response.status_code = 400

    return response


class Validator:
    def __init__(self, req: request) -> None:
        self._request = req

    def validate(self):
        print('common is good')
        return True


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

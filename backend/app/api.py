from flask import request, jsonify
from wtforms.validators import DataRequired
from app import app


class ValidationError(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            'message': self.message
        }


@app.errorhandler(ValidationError)
@app.errorhandler(Exception)
def handle_invalid_usage(error):
    if issubclass(error.__class__, ValidationError):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
    else:
        response = jsonify({'status_code': 413, 'message': 'polomalos'})

    return response


def validation_callback():
    print(request, '--- xXx ---> VALIDATION CALL <--- xXx ---')
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


class Api:
    API_PREFIX = 'api'
    API_VERSION = '1.0'

    def __init__(self, name: str, url_prefix: str = None) -> None:
        self.name = self._prepare_name(name)
        self.url_prefix = url_prefix

    def add_url_rule(self, rule: str, view_func, validator: Validator = None) -> None:
        rule = self._prepare_rule(rule)
        endpoint = self._prepare_endpoint(view_func)
        app.add_url_rule(rule, endpoint, view_func)
        if validator is not None:
            self._register_validator(endpoint, validator)

    def _prepare_name(self, name):
        return '{api_prefix}.{name}'.format(api_prefix=self.API_PREFIX, name=name)

    def _prepare_rule(self, rule: str) -> str:
        return '/{api_prefix}/v{api_version}{url_prefix}{rule}'.format(
            api_prefix=self.API_PREFIX,
            api_version=self.API_VERSION,
            url_prefix=self.url_prefix,
            rule=rule
        )

    def _prepare_endpoint(self, view_func) -> str:
        return '{api_name}.{view_name}'.format(api_name=self.name, view_name=view_func.__name__)

    def _register_validator(self, endpoint: str, validator: Validator):
        ValidatorFactory.register_validator(endpoint, validator)
        callbacks = app.before_request_funcs.setdefault(None, [])
        if validation_callback not in callbacks:
            callbacks.append(validation_callback)



class ApiKeyValidation:
    valid_api_key = 12345

    headers = {
        'Authorization': [DataRequired(), valid_api_key]
    }

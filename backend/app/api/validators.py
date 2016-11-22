from flask import request

from app.api.schemas import BaseSchema
from app.errors import Error, InvalidAttribute, BadRequest


def validation_callback():
    try:
        validator = ValidatorFactory.get_validator(request.endpoint)
        validator = validator(request)
    except KeyError as err:
        # todo: log
        print('Validator is not registered for ', err)
    else:
        validator.general()
        try:
            method = request.method.lower()
            validate_func = getattr(validator, method)
        except AttributeError as err:
            # todo: log
            print('Validator has no method ', err)
        else:
            validate_func()


class Validator:
    def __init__(self, req: request) -> None:
        self._request = req
        self._json = self._parse_json()

    def general(self):
        print('common is good')
        return True

    def _parse_json(self):
        try:
            return self._request.get_json()
        except Exception as e:
            raise BadRequest(Error(str(e)))

    def validate_schema(self, schema: BaseSchema.__class__, partial=None):
        '''
        :param bool|tuple partial: Whether to ignore missing fields. If its value is an iterable,
            only missing fields listed in that iterable will be ignored.
        '''
        errors = schema().validate(self._json, partial=partial)
        if self._request.method != 'POST' and 'uuid' not in self._json['data']:
            raise BadRequest(Error('Required UUID member is missing.'))
        if errors:
            exception = BadRequest()
            for attr, messages in errors.items():
                for msg in messages:
                    exception.add_error(InvalidAttribute(source=attr, detail=msg))
            raise exception

    def validate_uuid(self, url_param: str = 'uuid'):
        if self._request.view_args[url_param] != self._json['data']['uuid']:
            raise BadRequest(InvalidAttribute('uuid in url and uuid in json mismatch.'))


class ValidatorFactory:
    _validators = {}

    @classmethod
    def get_validator(cls, endpoint: str) -> Validator.__class__:
        # todo: exceptions
        return cls._validators[endpoint]

    @classmethod
    def register_validator(cls, endpoint: str, validator: Validator) -> None:
        # todo: exceptions
        cls._validators[endpoint] = validator

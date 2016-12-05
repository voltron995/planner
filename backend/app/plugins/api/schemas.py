from app.error_handlers.errors import Error
from marshmallow import Schema
from marshmallow import fields
from marshmallow import pre_load

from app.error_handlers.exceptions import APIBadRequest


class PluginActionSchema(Schema):
    _type = 'plugins'

    plugin_name = fields.Str(required=True)
    action_name = fields.Str(required=True)
    action_data = fields.Dict()

    @pre_load
    def process_input(self, json_input):
        if 'data' not in json_input:
            raise APIBadRequest(Error('Required DATA member is missing.'))

        data = json_input['data']
        if self._type != data['type']:
            raise APIBadRequest(Error('Invalid schema type.'))

        if 'attributes' not in data:
            raise APIBadRequest(Error('Required ATTRIBUTES member is missing.'))

        output = data['attributes']

        return output

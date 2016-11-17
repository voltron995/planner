from marshmallow import Schema
from marshmallow import fields
from marshmallow import pre_load

from app.errors import BadRequest, Error


class PluginActionSchema(Schema):
    _type = 'plugins'

    plugin_name = fields.Str(required=True)
    action_name = fields.Str(required=True)
    action_data = fields.Dict()

    @pre_load
    def process_input(self, json_input):
        if 'data' not in json_input:
            raise BadRequest(Error('Required DATA member is missing.'))

        data = json_input['data']
        if self._type != data['type']:
            raise BadRequest(Error('Invalid schema type.'))

        if 'attributes' not in data:
            raise BadRequest(Error('Required ATTRIBUTES member is missing.'))

        output = data['attributes']

        return output

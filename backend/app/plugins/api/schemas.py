from marshmallow import Schema
from marshmallow import fields


class PluginActionSchema(Schema):
    plugin_name = fields.Str(required=True)
    action_name = fields.Str(required=True)
    action_data = fields.Dict()

from marshmallow import fields
from marshmallow import validates_schema

from app.api.schemas import ModelSchema
from app.plugins.plugins import get_plugin


class ItemSchema(ModelSchema):
    plugin = fields.Str(required=True)
    attributes = fields.Dict(required=True)

    @validates_schema
    def validate_data(self, data):
        plugin = get_plugin(data['plugin'])
        plugin.item_schema().validate(data['attributes'])

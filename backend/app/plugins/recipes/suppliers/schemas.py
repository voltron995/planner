from marshmallow import fields

from app.api.schemas import ModelSchema


class SupplierSchema(ModelSchema):
    id = fields.Int()
    name = fields.String()
    contact = fields.String()

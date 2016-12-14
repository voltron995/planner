from marshmallow import fields

from app.api.schemas import ModelSchema
from ..suppliers.schemas import SupplierSchema


class ProductSupplierSchema(ModelSchema):
    price = fields.Int()
    supplier = fields.Nested(SupplierSchema)


class ProductSchema(ModelSchema):
    id = fields.Int()
    name = fields.String()
    quantity = fields.Int()
    ingredient_id = fields.Int()
    suppliers = fields.Nested(ProductSupplierSchema, many=True)

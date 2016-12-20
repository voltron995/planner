from marshmallow import Schema, fields

from app.api.schemas import ModelSchema
from ..products.schemas import ProductSchema


class CategorySchema(ModelSchema):
    id = fields.Int()
    name = fields.String()


class IngredientSchema(ModelSchema):
    id = fields.Int()
    name = fields.String()
    description = fields.String()
    image = fields.String()
    categories = fields.Nested(CategorySchema, many=True)
    products = fields.Nested(ProductSchema, many=True)
    dimension = fields.String()


class IngredientListSchema(Schema):
    quantity = fields.Int(required=True)
    ingredient = fields.Nested(IngredientSchema, required=True)

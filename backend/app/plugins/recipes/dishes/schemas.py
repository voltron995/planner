from marshmallow import Schema, fields

from ..ingredients.schemas import IngredientListSchema


class DishSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    description = fields.String()
    img_path = fields.String()
    ingredients = fields.Nested(
        IngredientListSchema,
        many=True,
        required=True
    )
    price = fields.String(dump_only=True)
    event_id = fields.Str(required=True)


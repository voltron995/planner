from marshmallow import Schema, fields, pre_load, validate
from marshmallow.exceptions import ValidationError
from ..ingredients.schemas import IngredientListSchema
from .models import Recipe

class CategorySchema(Schema):
    id = fields.Int()
    name = fields.String()


class RecipeSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    description = fields.String()
    img_path = fields.String()
    categories = fields.Nested(CategorySchema, many=True)
    ingredients = fields.Nested(
    	IngredientListSchema,
    	many=True,
        required=True)
    price = fields.String(dump_only=True)

    @pre_load
    def check_name(self, data):
        recipe = Recipe.query.filter_by(name=data['name']).first()
        if recipe:
            raise ValidationError('Name: Duplicated value')
        return data

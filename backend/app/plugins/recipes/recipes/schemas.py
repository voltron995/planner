from flask import url_for
from marshmallow import fields
from marshmallow import post_dump

from app.api.schemas import ModelSchema
from app.uploads import groups
from app.uploads.manager import UploadsManager
from ..ingredients.schemas import IngredientListSchema


class CategorySchema(ModelSchema):
    id = fields.Int()
    name = fields.String()


class RecipeSchema(ModelSchema):
    id = fields.Int()
    name = fields.String(required=True)
    description = fields.String()
    image = fields.String()
    categories = fields.Nested(CategorySchema, many=True)
    ingredients = fields.Nested(
        IngredientListSchema,
        many=True,
        required=True)
    price = fields.String(dump_only=True)

    @post_dump(pass_many=True)
    def post_dump_callback(self, data, many):
        if not many:
            return self._add_image_link(data)
        else:
            return [self._add_image_link(item) for item in data]

    # todo: do it better
    def _add_image_link(self, item):
        if item['image']:
            item['image_link'] = UploadsManager.get_link(item['image'], groups.RECIPE_IMAGES)
        else:
            item['image_link'] = url_for('static', filename='assets/recipe-default.jpg')
        return item



from flask import url_for
from marshmallow import Schema, fields
from marshmallow import post_dump

from app.uploads import groups
from app.uploads.manager import UploadsManager
from ..ingredients.schemas import IngredientListSchema


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

    @post_dump(pass_many=True)
    def post_dump_callback(self, data, many):
        if not many:
            return self._add_image_link(data)
        else:
            return [self._add_image_link(item) for item in data]

    # todo: do it better
    def _add_image_link(self, item):
        if item['img_path']:
            item['image_link'] = UploadsManager.get_link(item['img_path'], groups.RECIPE_IMAGES)
        else:
            item['image_link'] = url_for('static', filename='assets/recipe-default.jpg')
        return item

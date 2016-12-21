from flask import url_for
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import validates

from app.api.schemas import ModelSchema
from app.events.models import Event
from app.plugins.recipes.ingredients.schemas import IngredientListSchema
from app.uploads import groups
from app.uploads.manager import UploadsManager


class DishSchema(ModelSchema):
    id = fields.Int()
    name = fields.String(required=True)
    description = fields.String()
    image = fields.String()
    ingredients = fields.Nested(
        IngredientListSchema,
        many=True,
        required=True
    )
    price = fields.String(dump_only=True)
    event_id = fields.Str(required=True)

    @validates('event_id')
    def validate_event(self, data):
        Event.get_or_404(data)

    @post_dump(pass_many=True)
    def post_dump_callback(self, data, many):
        if not many:
            return self._add_image_link(data)
        else:
            return [self._add_image_link(item) for item in data]

    # todo: do it better
    def _add_image_link(self, item):
        if item['image']:
            item['image_link'] = UploadsManager.get_link(item['image'], groups.DISH_IMAGES)
        else:
            item['image_link'] = url_for('static', filename='assets/dish-default.jpg')
        return item


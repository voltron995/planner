from marshmallow import fields
from marshmallow import validates

from app.api.schemas import ModelSchema
from app.events.models import Event
from app.plugins.recipes.ingredients.schemas import IngredientListSchema


class DishSchema(ModelSchema):
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

    @validates('event_id')
    def validate_event(self, data):
        Event.get_or_404(data)

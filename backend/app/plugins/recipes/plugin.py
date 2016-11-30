from app.plugins.plugins import register, BasePlugin
from app.plugins.recipes.dishes.schemas import DishSchema


@register
class Recipes(BasePlugin):
    name = 'recipes'
    port = '6001'
    host = '127.0.0.1'
    item_schema = DishSchema

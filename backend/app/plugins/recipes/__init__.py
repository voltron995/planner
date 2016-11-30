from app.api import Api
from app.plugins.plugins import BasePlugin, register

api_recipes = Api('plugins.recipes', url_prefix='/plugins/recipes')


@register
class Recipes(BasePlugin):
    name = 'recipes'
    port = '6000'
    host = '127.0.0.1'


from . import dishes, recipes, suppliers, ingredients, products

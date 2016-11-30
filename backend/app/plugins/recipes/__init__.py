from app.api import Api
from app.plugins.plugins import BasePlugin, register

api_recipes = Api('plugins.recipes', url_prefix='/plugins/recipes')


@register
class Recipes(BasePlugin):
    name = 'recipes'
    port = '5000'
    host = '192.168.96.154'


from . import dishes

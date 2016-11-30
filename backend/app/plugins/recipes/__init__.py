from app.api import Api

api_recipes = Api('plugins.recipes', url_prefix='/plugins/recipes')

from . import dishes, recipes, suppliers, ingredients, products, plugin

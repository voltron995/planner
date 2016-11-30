from app.api import Api

api_recipes = Api('plugins.recipes', url_prefix='/plugins/recipes')

from .import plugin
from . import dishes

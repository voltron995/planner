from app.plugins.recipes.plugin import Recipes
from app.plugins.recipes.recipes.schemas import RecipeSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class RecipesList(ListCreateView):
    plugin = Recipes
    schema = RecipeSchema
    actions = {
        'GET': 'RecipeList_get',
    }


class RecipesSingle(ReadUpdateDeleteView):
    plugin = Recipes
    schema = RecipeSchema
    actions = {
        'GET': 'RecipeEntity_get',
    }

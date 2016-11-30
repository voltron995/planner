from app.plugins.plugins import get_plugin
from app.plugins.recipes.recipes.schemas import RecipeSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class RecipesList(ListCreateView):
    plugin = get_plugin('recipes')
    schema = RecipeSchema
    actions = {
        'GET': 'RecipeList_get',
    }


class RecipesSingle(ReadUpdateDeleteView):
    plugin = get_plugin('recipes')
    schema = RecipeSchema
    actions = {
        'GET': 'RecipeEntity_get',
    }

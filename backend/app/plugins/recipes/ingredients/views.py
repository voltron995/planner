from app.plugins.plugins import get_plugin
from app.plugins.recipes.ingredients.schemas import IngredientSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class IngredientsList(ListCreateView):
    plugin = get_plugin('recipes')
    schema = IngredientSchema
    actions = {
        'GET': 'RecipeList_get',
    }


class IngredientsSingle(ReadUpdateDeleteView):
    plugin = get_plugin('recipes')
    schema = IngredientSchema
    actions = {
        'GET': 'RecipeEntity_get',
    }

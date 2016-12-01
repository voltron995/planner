from app.plugins.recipes.ingredients.schemas import IngredientSchema
from app.plugins.recipes.plugin import Recipes
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class IngredientsList(ListCreateView):
    plugin = Recipes
    schema = IngredientSchema
    actions = {
        'GET': 'RecipeList_get',
    }


class IngredientsSingle(ReadUpdateDeleteView):
    plugin = Recipes
    schema = IngredientSchema
    actions = {
        'GET': 'RecipeEntity_get',
    }

from app.plugins.recipes.plugin import Recipes
from app.plugins.recipes.recipes.schemas import RecipeSchema, CategorySchema
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

class CategoryList(ListCreateView):
    plugin = Recipes
    schema = CategorySchema
    actions = {
        'GET': 'RecipeCategory_get',
    }

class CategorySingle(ReadUpdateDeleteView):
    plugin = Recipes
    schema = CategorySchema
    actions = {
        'GET': 'RecipeCategoryEntity_get',
    }

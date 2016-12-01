from app.plugins.plugins import get_plugin
from app.plugins.recipes.plugin import Recipes
from app.plugins.recipes.products.schemas import ProductSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class ProductsList(ListCreateView):
    plugin = Recipes
    schema = ProductSchema
    actions = {
        'GET': 'ProductList_get',
    }


class ProductsSingle(ReadUpdateDeleteView):
    plugin = Recipes
    schema = ProductSchema
    actions = {
        'GET': 'ProductEntity_get',
    }

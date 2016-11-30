from app.plugins.plugins import get_plugin
from app.plugins.recipes.products.schemas import ProductSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class ProductsList(ListCreateView):
    plugin = get_plugin('recipes')
    schema = ProductSchema
    actions = {
        'GET': 'ProductList_get',
    }


class ProductsSingle(ReadUpdateDeleteView):
    plugin = get_plugin('recipes')
    schema = ProductSchema
    actions = {
        'GET': 'ProductEntity_get',
    }

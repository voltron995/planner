from app.plugins.plugins import get_plugin
from app.plugins.recipes.dishes.schemas import DishSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class DishesList(ListCreateView):
    plugin = get_plugin('recipes')
    schema = DishSchema
    actions = {
        'GET': 'dish_list',
        'POST': 'dish_create',
    }


class DishesSingle(ReadUpdateDeleteView):
    plugin = get_plugin('recipes')
    schema = DishSchema
    actions = {
        'GET': 'dish_get',
        'PUT': 'dish_update',
        'DELETE': 'dish_delete',
    }

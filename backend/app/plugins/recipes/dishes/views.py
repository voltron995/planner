from app.plugins.plugins import get_plugin
from app.plugins.recipes.dishes.schemas import DishSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class DishesList(ListCreateView):
    plugin = 'recipes'
    schema = DishSchema
    actions = {
        'GET': 'DishList_get',
        'POST': 'DishList_create',
    }


class DishesSingle(ReadUpdateDeleteView):
    plugin = 'recipes'
    schema = DishSchema
    actions = {
        'GET': 'DishEntity_get',
        'PUT': 'DishEntity_update',
        'DELETE': 'DishEntity_delete',
    }

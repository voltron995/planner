from app.plugins.recipes.dishes.schemas import DishSchema
from app.plugins.recipes.plugin import Recipes
from app.plugins.views import ListCreateItemView, ReadUpdateDeleteItemView
from app.uploads import groups


class DishesList(ListCreateItemView):
    plugin = Recipes
    schema = DishSchema
    upload_group = groups.DISH_IMAGES
    actions = {
        'GET': 'DishList_get',
        'POST': 'DishList_create',
    }


class DishesSingle(ReadUpdateDeleteItemView):
    plugin = Recipes
    schema = DishSchema
    upload_group = groups.DISH_IMAGES
    actions = {
        'GET': 'DishEntity_get',
        'PUT': 'DishEntity_update',
        'DELETE': 'DishEntity_delete',
    }

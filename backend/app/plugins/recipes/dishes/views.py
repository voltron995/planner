from flask import request

from app import db
from app.api import response
from app.items.models import Item
from app.plugins.recipes.dishes.schemas import DishSchema
from app.plugins.recipes.plugin import Recipes
from app.plugins.views import ListCreateItemView, ReadUpdateDeleteItemView
from app.uploads import groups
from app.uploads.manager import UploadsManager


class DishesList(ListCreateItemView):
    plugin = Recipes
    schema = DishSchema
    actions = {
        'GET': 'DishList_get',
        'POST': 'DishList_create',
    }

    def post(self, **view_args):
        self._validate_schema()

        json = request.json
        ms_response = self.plugin.execute_action(self.actions['POST'], view_args, **json)
        if ms_response.ok:
            Item.create(plugin=self.plugin.name, plugin_item_id=ms_response.data.get('id'), event_id=json['event_id'])
            db.session.commit()

            image_uuid = json.get('image')
            if image_uuid:
                image = UploadsManager.get_file(image_uuid, groups.RECIPE_IMAGES)
                UploadsManager.copy_file(image, groups.DISH_IMAGES)

            return response.success(data=ms_response.data, schema=self.schema)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


class DishesSingle(ReadUpdateDeleteItemView):
    plugin = Recipes
    schema = DishSchema
    actions = {
        'GET': 'DishEntity_get',
        'PUT': 'DishEntity_update',
        'DELETE': 'DishEntity_delete',
    }

    def put(self, **view_args):
        self._validate_schema()

        json = request.json
        ms_response = self.plugin.execute_action(self.actions['PUT'], view_args, **json)

        if ms_response.ok:
            image_uuid = json.get('image')
            if image_uuid and UploadsManager.is_tmp_file(image_uuid):
                image = UploadsManager.get_tmp_file(image_uuid)
                UploadsManager.move_file(image, groups.DISH_IMAGES)

            return response.success(data=ms_response.data, schema=self.schema)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


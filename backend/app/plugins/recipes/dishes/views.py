from flask import request

from app import db
from app.api import response
from app.items.models import Item
from app.plugins.recipes.dishes.schemas import DishSchema
from app.plugins.recipes.plugin import Recipes
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class DishesList(ListCreateView):
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
            return response.success(data=ms_response.data, schema=self.schema)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


class DishesSingle(ReadUpdateDeleteView):
    plugin = Recipes
    schema = DishSchema
    actions = {
        'GET': 'DishEntity_get',
        'PUT': 'DishEntity_update',
        'DELETE': 'DishEntity_delete',
    }

    def delete(self, **view_args):
        ms_response = self.plugin.execute_action(self.actions['DELETE'], view_args)
        if ms_response.ok:
            Item.get_by(plugin_item_id=view_args['id']).delete()
            db.session.commit()
            return response.success()
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


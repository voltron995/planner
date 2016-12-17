from flask import request

from app import db
from app.api import response
from app.api.views import BaseView
from app.items.models import Item
from app.plugins.plugins import get_plugin
from app.uploads.manager import UploadsManager


class PluginView(BaseView):
    plugin = None  # type: str
    actions = None  # type: dict
    upload_group = None  # type: str

    def __init__(self):
        super().__init__()
        self.plugin = get_plugin(self.__class__.plugin.name)

    def _execute_action(self, method, view_args, data, many=False):
        if method in ('GET', 'DELETE'):
            pass
        else:
            self._validate_schema()

        if not data:
            data = {}

        ms_response = self.plugin.execute_action(self.actions[method], view_args, **data)

        if ms_response.ok:
            return response.success(data=ms_response.data, schema=self.schema, many=many)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


class ListCreateView(PluginView):
    methods = ['GET', 'POST']

    def get(self, **view_args):
        return self._execute_action('GET', view_args, request.args, many=True)

    def post(self, **view_args):
        return self._execute_action('POST', view_args, request.json)


class ReadUpdateDeleteView(PluginView):
    methods = ['GET', 'PUT', 'DELETE']

    def get(self, **view_args):
        return self._execute_action('GET', view_args, request.args)

    def put(self, **view_args):
        return self._execute_action('PUT', view_args, request.json)

    def delete(self, **view_args):
        return self._execute_action('DELETE', view_args, request.get_json(silent=True))


class ListCreateItemView(ListCreateView):
    methods = ['POST', 'GET']

    def post(self, **view_args):
        self._validate_schema()

        json = request.json
        ms_response = self.plugin.execute_action(self.actions['POST'], view_args, **json)
        if ms_response.ok:
            Item.create(plugin=self.plugin.name, plugin_item_id=ms_response.data.get('id'), event_id=json['event_id'])
            db.session.commit()

            if 'img_path' in json:
                image_uuid = json['img_path']
                image = UploadsManager.get_tmp_file(image_uuid)
                UploadsManager.move_file(image, self.upload_group)

            return response.success(data=ms_response.data, schema=self.schema)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


class ReadUpdateDeleteItemView(ReadUpdateDeleteView):

    def put(self, **view_args):
        self._validate_schema()

        json = request.json
        ms_response = self.plugin.execute_action(self.actions['PUT'], view_args, **json)

        if ms_response.ok:
            image_uuid = json.get('img_path')
            if image_uuid and UploadsManager.is_tmp_file(image_uuid):
                image = UploadsManager.get_tmp_file(image_uuid)
                UploadsManager.move_file(image, self.upload_group)

            return response.success(data=ms_response.data, schema=self.schema)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)

    def delete(self, **view_args):
        ms_response = self.plugin.execute_action(self.actions['DELETE'], view_args)
        if ms_response.ok:
            Item.get_by(plugin_item_id=view_args['id']).delete()
            db.session.commit()
            return response.success()
        else:
            return response.error(ms_response.status_code, *ms_response.errors)

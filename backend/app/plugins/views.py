from flask import request

from app.api import response
from app.api.views import BaseView
from app.plugins.plugins import BasePlugin, get_plugin


class PluginView(BaseView):
    plugin = None  # type: str
    actions = None  # type: dict

    def __init__(self):
        super().__init__()
        self.plugin = get_plugin(self.__class__.plugin)

    def _execute_action(self, method, view_args, data, many=False):
        self._validate_schema()

        if not data:
            data = {}

        ms_response = self.plugin.execute_action(self.actions[method], view_args, **data)

        if ms_response.ok:
            return response.success(data=ms_response.data, schema=self.schema, many=many)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)


def response_decorator(method):
    def wrap(self, **view_args):

        self._validate_schema()
        ms_response = method(self, **view_args)

        if ms_response.ok:
            return response.success(data=ms_response.data, schema=self.schema)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)

    return wrap


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

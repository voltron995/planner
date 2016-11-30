from flask import request

from app.api import response
from app.api.views import BaseView
from app.plugins.plugins import BasePlugin


class PluginView(BaseView):
    plugin = None  # type: BasePlugin
    actions = None  # type: dict

    def _execute_action(self, method, view_args, **data):
        self._validate_schema()

        ms_response = self.plugin.execute_action(self.actions[method], view_args, **data)

        if ms_response.ok:
            return response.success(data=ms_response.data, schema=self.schema)
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
        return self._execute_action('GET', view_args, **request.args)

    def post(self, **view_args):
        return self._execute_action('POST', view_args, **request.json)


class ReadUpdateDeleteView(PluginView):
    methods = ['GET', 'PUT', 'DELETE']

    def get(self, **view_args):
        return self._execute_action('GET', view_args, **request.args)

    def put(self, **view_args):
        return self._execute_action('PUT', view_args, **request.json)

    def delete(self, **view_args):
        return self._execute_action('DELETE', view_args, **request.json)

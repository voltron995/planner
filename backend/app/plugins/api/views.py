from flask import request
from flask.views import MethodView

from app.api import response
from app.plugins.plugins import PluginFactory


class PluginAction(MethodView):
    def post(self):
        attrs = request.json['data']['attributes']

        plugin = PluginFactory.get_plugin(attrs.get('plugin_name'))
        ms_response = plugin.execute_action(attrs.get('action_name'), **attrs.get('action_data'))

        if ms_response.ok:
            return response.success(data=ms_response.data)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)

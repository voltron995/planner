from flask import request
from flask.views import MethodView

from app.api import response
from app.plugins.plugins import PluginFactory


# todo: This should be totally rewritten!

class PluginAction(MethodView):
    def post(self):
        data = request.json
        plugin = PluginFactory.get_plugin(data.get('plugin_name'))
        ms_response = plugin.execute_action(data.get('action_name'), **data.get('action_data'))

        if ms_response.ok:
            return response.success(data=ms_response.data)
        else:
            return response.error(ms_response.status_code, *ms_response.errors)

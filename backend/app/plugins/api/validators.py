from app.error_handlers.errors import InvalidAttribute

from app.api.validators import Validator
from app.error_handlers.exceptions import APIBadRequest
from app.plugins.api.schemas import PluginActionSchema
from app.plugins.plugins import PluginFactory


class PluginAction(Validator):
    def post(self):
        self.validate_schema(PluginActionSchema)

        attrs = self._json['data']['attributes']

        plugin = PluginFactory.get_plugin(attrs.get('plugin_name'))
        if not plugin:
            raise APIBadRequest(InvalidAttribute('Plugin does not exist.'))

        if not plugin.is_action_exist(attrs('action_name')):
            raise APIBadRequest(InvalidAttribute('Plugin does not have action.'))

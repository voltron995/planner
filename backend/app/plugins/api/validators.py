from app.api.validators import Validator
from app.plugins.api.schemas import PluginActionSchema


class PluginAction(Validator):
    def post(self):
        self.validate_schema(PluginActionSchema)

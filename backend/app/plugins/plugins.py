from app.errors import Error, DefaultException
from app.plugins.msclient import MSClient


class BasePlugin:
    name = ''
    port = ''
    host = ''

    actions = {}

    def __init__(self):
        self._init_actions()

    def execute_action(self, action_name: str, **data):
        url = self._get_action_url(action_name)
        method = self._get_action_method(action_name)
        return MSClient.send_request(url, data, method)

    def is_action_exist(self, action_name):
        return action_name in self.actions

    def _init_actions(self):
        url = self._get_url('/actions')
        response = MSClient.send_request(url)
        if response.ok:
            # todo: validate json schema for actions
            self.actions = response.data

    def _get_url(self, path: str = '/') -> str:
        return 'http://{host}:{port}{path}'.format(host=self.host, port=self.port, path=path)

    def _get_action_url(self, action_name):
        return self._get_url(self.actions[action_name]['path'])

    def _get_action_method(self, action_name):
        return self.actions[action_name]['method']


class Recipes(BasePlugin):
    name = 'recipes'
    port = '5000'
    host = '192.168.96.154'


class Custom(BasePlugin):
    name = 'custom'
    port = '5050'
    host = '127.0.0.1'


plugins = [
    Custom
]


class PluginFactory:
    _plugins = {}

    @classmethod
    def get_plugin(cls, name: str) -> BasePlugin:
        return cls._plugins.get(name, None)

    @classmethod
    def register_plugin(cls, plugin: BasePlugin):
        cls._plugins[plugin.name] = plugin


def register_plugins():
    for plugin_class in plugins:
        if issubclass(plugin_class, BasePlugin):
            PluginFactory.register_plugin(plugin_class())

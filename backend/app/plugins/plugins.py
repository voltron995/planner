import re

from app import app
from app.error_handlers.errors import ElementNotFound
from app.error_handlers.exceptions import APINotFound
from app.plugins.msclient import MSClient

# A dictionary with plugins. The key of the dictionary
# is the name of the plugin and the value is the plugin
# class.
_plugins = {}


def register_plugin(plugin_class):
    """
    :type plugin_class: BasePlugin
    """
    _plugins[plugin_class.name] = plugin_class()


def get_plugin(name: str):
    """
    Returns a plugin instance.
    :param name: str
    :return: BasePlugin
    """
    try:
        return _plugins[name]
    except KeyError:
        raise APINotFound(ElementNotFound(detail='The plugin cannot be found'))


def register(cls):
    """
    Decorator to register plugin.
    :param cls:
    :return:
    """
    if cls.name:
        register_plugin(cls)
    return cls


class BasePlugin:
    name = ''
    port = ''
    host = ''

    actions = {}

    def __init__(self):
        config = app.config['PLUGINS'].get(self.name)
        if not config:
            raise Exception("Plugin not found.")
        self.port = config['port']
        self.host = config['host']
        self._init_actions()

    def execute_action(self, action_name: str, view_args: dict = None, **data):
        url = self._get_action_url(action_name, view_args)
        method = self._get_action_method(action_name)
        if method == 'GET':
            return MSClient.send_request(url, method=method, params=data)
        return MSClient.send_request(url, method=method, json=data)

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

    def _get_action_url(self, action_name: str, view_args: dict = None):
        view_args = [] if not view_args else list(view_args.values())
        url = self._get_url(self.actions[action_name]['path'])
        return re.sub(r'<.+?>', lambda match: str(view_args.pop(0)), url)

    def _get_action_method(self, action_name):
        return self.actions[action_name]['method']

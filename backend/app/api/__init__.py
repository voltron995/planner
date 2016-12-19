from app import app
from app.api.permitters import Permitter, PermitterFactory, permission_callback


class Api:
    API_PREFIX = 'api'
    API_VERSION = '1.0'

    def __init__(self, name: str, url_prefix: str = None):
        self.name = self._prepare_name(name)
        self.url_prefix = url_prefix

    def add_url_rule(
            self,
            rule: str,
            view_func,
            permitter: Permitter = None
    ) -> None:
        rule = self._prepare_rule(rule)
        endpoint = self._prepare_endpoint(view_func)
        app.add_url_rule(rule, endpoint, view_func)
        if permitter:
            self._register_permitter(endpoint, permitter)

    def _prepare_name(self, name):
        return '{api_prefix}.{name}'.format(api_prefix=self.API_PREFIX, name=name)

    def _prepare_rule(self, rule: str) -> str:
        return '/{api_prefix}/v{api_version}{url_prefix}{rule}'.format(
            api_prefix=self.API_PREFIX,
            api_version=self.API_VERSION,
            url_prefix=self.url_prefix,
            rule=rule
        )

    def _prepare_endpoint(self, view_func) -> str:
        return '{api_name}.{view_name}'.format(api_name=self.name, view_name=view_func.__name__)

    def _register_permitter(self, endpoint: str, permitter: Permitter):
        PermitterFactory.register_permitter(endpoint, permitter)
        callbacks = app.before_request_funcs.setdefault(self.name, [])
        if permission_callback not in callbacks:
            callbacks.append(permission_callback)

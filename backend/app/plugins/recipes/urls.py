from app.plugins.api import api_plugins, permitters, views

api_plugins.add_url_rule(
    '/',
    view_func=views.PluginAction.as_view('plugin_action'),
    permitter=permitters.PluginAction,
)


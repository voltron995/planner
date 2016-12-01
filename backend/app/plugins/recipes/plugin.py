from app.plugins.plugins import register, BasePlugin


@register
class Recipes(BasePlugin):
    name = 'recipes'
    port = '6001'
    host = '127.0.0.1'

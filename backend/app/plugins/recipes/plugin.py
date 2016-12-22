from app.plugins.plugins import register, BasePlugin


@register
class Recipes(BasePlugin):
    name = "recipes"

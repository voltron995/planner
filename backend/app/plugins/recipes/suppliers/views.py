from app.plugins.plugins import get_plugin
from app.plugins.recipes.plugin import Recipes
from app.plugins.recipes.suppliers.schemas import SupplierSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class SuppliersList(ListCreateView):
    plugin = Recipes
    schema = SupplierSchema
    actions = {
        'GET': 'SupplierList_get',
    }


class SuppliersSingle(ReadUpdateDeleteView):
    plugin = Recipes
    schema = SupplierSchema
    actions = {
        'GET': 'SupplierEntity_get',
    }

from app.plugins.plugins import get_plugin
from app.plugins.recipes.suppliers.schemas import SupplierSchema
from app.plugins.views import ListCreateView, ReadUpdateDeleteView


class SuppliersList(ListCreateView):
    plugin = get_plugin('recipes')
    schema = SupplierSchema
    actions = {
        'GET': 'SupplierList_get',
    }


class SuppliersSingle(ReadUpdateDeleteView):
    plugin = get_plugin('recipes')
    schema = SupplierSchema
    actions = {
        'GET': 'SupplierEntity_get',
    }

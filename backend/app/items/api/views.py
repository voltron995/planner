from app.api.views import ListCreateView, ReadUpdateDeleteView
from app.items.api.schemas import ItemSchema
from app.items.models import Item


class ItemList(ListCreateView):
    model = Item
    schema = ItemSchema


class ItemSingle(ReadUpdateDeleteView):
    model = Item
    schema = ItemSchema

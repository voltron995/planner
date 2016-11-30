from app.items.api import api_items
from app.items.api import permitters
from app.items.api import views

api_items.add_url_rule(
    '/',
    view_func=views.ItemList.as_view('list'),
    permitter=permitters.ItemListPermitter
)
api_items.add_url_rule(
    '/<id>',
    view_func=views.ItemSingle.as_view('single'),
    permitter=permitters.ItemSinglePermitter
)


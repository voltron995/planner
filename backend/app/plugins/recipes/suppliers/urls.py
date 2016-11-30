from app.plugins.recipes import api_recipes
from app.plugins.recipes.suppliers import permitters
from app.plugins.recipes.suppliers import views

api_recipes.add_url_rule(
    '/suppliers/',
    view_func=views.SuppliersList.as_view('suppliers_list'),
    permitter=permitters.SuppliersListPermitter,
)

api_recipes.add_url_rule(
    '/suppliers/<id>',
    view_func=views.SuppliersSingle.as_view('suppliers_single'),
    permitter=permitters.SuppliersSinglePermitter,
)

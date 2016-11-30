from app.plugins.recipes import api_recipes
from app.plugins.recipes.products import permitters
from app.plugins.recipes.products import views

api_recipes.add_url_rule(
    '/products/',
    view_func=views.ProductsList.as_view('products_list'),
    permitter=permitters.ProductsListPermitter,
)

api_recipes.add_url_rule(
    '/products/<id>',
    view_func=views.ProductsSingle.as_view('products_single'),
    permitter=permitters.ProductsSinglePermitter,
)

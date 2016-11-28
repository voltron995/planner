from app.plugins.recipes import api_recipes
from app.plugins.recipes.dishes import permitters
from app.plugins.recipes.dishes import views

api_recipes.add_url_rule(
    '/dishes/',
    view_func=views.DishesList.as_view('dishes_list'),
    permitter=permitters.DishesListPermitter,
)

api_recipes.add_url_rule(
    '/dishes/<id>',
    view_func=views.DishesSingle.as_view('dishes_single'),
    permitter=permitters.DishesSinglePermitter,
)

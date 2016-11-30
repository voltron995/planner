from app.plugins.recipes import api_recipes
from app.plugins.recipes.ingredients import permitters
from app.plugins.recipes.ingredients import views

api_recipes.add_url_rule(
    '/ingredients/',
    view_func=views.IngredientsList.as_view('ingredients_list'),
    permitter=permitters.IngredientsListPermitter,
)

api_recipes.add_url_rule(
    '/ingredients/<id>',
    view_func=views.IngredientsSingle.as_view('ingredients_single'),
    permitter=permitters.IngredientsSinglePermitter,
)

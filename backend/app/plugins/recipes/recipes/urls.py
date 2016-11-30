from app.plugins.recipes import api_recipes
from app.plugins.recipes.recipes import permitters
from app.plugins.recipes.recipes import views

api_recipes.add_url_rule(
    '/recipes/',
    view_func=views.RecipesList.as_view('recipes_list'),
    permitter=permitters.RecipesListPermitter,
)

api_recipes.add_url_rule(
    '/recipes/<id>',
    view_func=views.RecipesSingle.as_view('recipes_single'),
    permitter=permitters.RecipesSinglePermitter,
)

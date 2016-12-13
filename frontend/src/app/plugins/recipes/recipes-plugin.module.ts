import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {IngredientService} from "./ingredients/services/ingredients.service";
import {RecipeDetailComponent} from "./recipes/components/recipe-detail/recipe-detail.component";
import {IngredientsListComponent} from "./ingredients/components/ingredients-list.component";
import {BrowserModule} from "@angular/platform-browser";
import {RecipesPluginComponent} from "./recipes-plugin.component";
import {CategoryService} from "./categories/services/category.service";
import {RecipeService} from "./recipes/services/recipe.service";
import {CategoriesComponent} from "./categories/components/categories/categories.component";
import {RecipesComponent} from "./recipes/components/recipes/recipes.component";

@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        RecipesPluginComponent,
        RecipeDetailComponent,
        IngredientsListComponent
        CategoriesComponent,
        RecipesComponent,
    ],
    providers: [
        DishService,
        CategoryService,
        RecipeService,
        IngredientService
    ],
    exports: [
        RecipesPluginComponent,
        CategoryListComponent,
        RecipeDetailComponent,
        IngredientsListComponent

    ]
})
export class RecipesPluginModule {}

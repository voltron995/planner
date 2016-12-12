import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {CategoryService} from "./categories/services/category.service";
import {RecipeService} from "./recipes/services/recipe.service";
import {IngredientService} from "./ingredients/services/ingredients.service";


import {RecipeListComponent} from "./recipes/components/recipelist/recipelist.component";
import {RecipeDetailComponent} from "./recipes/components/recipe-detail/recipe-detail.component";
import {CategoryListComponent} from "./categories/components/categorylist/categorylist.component";
import {IngredientsListComponent} from "./ingredients/components/ingredients-list.component";
import {BrowserModule} from "@angular/platform-browser";
import {RecipesPluginComponent} from "./recipes-plugin.component";
import {PluginsFactory} from "../plugins-factory";
import {RecipesPlugin} from "./recipes-plugin";

@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        RecipesPluginComponent,
        CategoryListComponent,
        RecipeListComponent,
        RecipeDetailComponent,
        IngredientsListComponent
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
        RecipeListComponent,
        RecipeDetailComponent,
        IngredientsListComponent


    ]
})
export class RecipesPluginModule {}

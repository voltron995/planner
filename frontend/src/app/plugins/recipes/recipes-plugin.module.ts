import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {BrowserModule} from "@angular/platform-browser";
import {RecipesPluginComponent} from "./recipes-plugin.component";
import {CategoryService} from "./categories/services/category.service";
import {RecipeService} from "./recipes/services/recipe.service";
import {CategoriesComponent} from "./categories/components/categories/categories.component";
import {RecipesComponent} from "./recipes/components/recipes/recipes.component";
import {RecipeComponent} from "./recipes/components/recipe/recipe.component";
import {MasonryModule} from "angular2-masonry/src/module";


@NgModule({
    imports: [
        BrowserModule,
        MasonryModule
    ],
    declarations: [
        RecipesPluginComponent,
        CategoriesComponent,
        RecipeComponent,
        RecipesComponent,
    ],
    providers: [
        DishService,
        RecipeService,
        CategoryService
    ],
    exports: [
        RecipesPluginComponent
    ]
})
export class RecipesPluginModule {}

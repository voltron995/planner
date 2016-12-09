import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {BrowserModule} from "@angular/platform-browser";
import {RecipesPluginComponent} from "./recipes-plugin.component";
import {CategoryListComponent} from "./categories/components/categorylist.component";
import {CategoryService} from "./categories/services/category.service";
import {RecipeService} from "./recipes/services/recipe.service";


@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        RecipesPluginComponent,
        CategoryListComponent,
    ],
    providers: [
        DishService,
        RecipeService,
        CategoryService
    ],
    exports: [
        RecipesPluginComponent,
        CategoryListComponent
    ]
})
export class RecipesPluginModule {}

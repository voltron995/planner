import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {PluginComponent} from "./plugin.component";
import {BrowserModule} from "@angular/platform-browser";
import {RecipeService} from "./recipes/services/recipe.service";
import {CategoryService} from "./categories/services/category.service";
import {CategoryListComponent} from "./categories/components/categorylist.component";

@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        PluginComponent,
        CategoryListComponent,
    ],
    providers: [
        DishService,
        RecipeService,
        CategoryService
    ],
    exports: [
        PluginComponent,
        CategoryListComponent
    ]
})
export class RecipesPlugin {
}

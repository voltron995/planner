import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {PluginComponent} from "./plugin.component";
import {BrowserModule} from "@angular/platform-browser";
import {RecipeService} from "./recipes/services/recipe.service";

@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        PluginComponent,
    ],
    providers: [
        DishService,
        RecipeService
    ],
    exports: [
        PluginComponent
    ]
})
export class RecipesPlugin {
}

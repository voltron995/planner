import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {BrowserModule} from "@angular/platform-browser";

import {RecipesPluginComponent} from "./recipes-plugin.component";
import {PluginsFactory} from "../plugins-factory";
import {RecipesPlugin} from "./recipes-plugin";

>>>>>>> 6c7a5ce01986bc9e6a31015e8959179b62232e3d:frontend/src/app/plugins/recipes/recipes-plugin.module.ts

@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        PluginComponent,
        RecipesPluginComponent,
    ],
    providers: [
        DishService,
        RecipeService,
        CategoryService
    ],
    exports: [
        PluginComponent,
        RecipesPluginComponent
    ]
})
export class RecipesPluginModule {}

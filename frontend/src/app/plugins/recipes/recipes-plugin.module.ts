import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
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
    ],
    providers: [
        DishService,
    ],
    exports: [
        RecipesPluginComponent
    ]
})
export class RecipesPluginModule {}

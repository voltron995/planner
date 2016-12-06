import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {PluginComponent} from "./plugin.component";
import {BrowserModule} from "@angular/platform-browser";


@NgModule({
    imports: [
        BrowserModule
    ],
    declarations: [
        PluginComponent,
    ],
    providers: [
        DishService,
    ],
    exports: [
        PluginComponent
    ]
})
export class RecipesPlugin {
}

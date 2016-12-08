import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";


@NgModule({
    providers: [
        DishService,
    ],
})
export class RecipesModule {
}

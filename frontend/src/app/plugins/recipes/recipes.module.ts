import {NgModule} from '@angular/core';
import {DishService} from "./dishes/services/dish.service";
import {RecipeService} from "./recipes/services/recipe.service";


@NgModule({
    providers: [
        DishService,
        RecipeService
    ],
})
export class RecipesModule {
}

import {Component, Input, OnInit} from '@angular/core';
import {Recipe} from '../../models/recipe'
import {DishService} from "../../../dishes/services/dish.service";
@Component({
    selector: 'recipe',
    templateUrl: 'recipe.component.html',
    styleUrls: [
        'recipe.component.css'
    ],

})

export class RecipeComponent {

    @Input()
    recipe: Recipe;

    @Input()
    eventId: string;

    constructor(
        private dishService: DishService
    ) {}

    postDish() {

        let data = {
            name: this.recipe.name,
            description: this.recipe.description,
            // img_path:this.recipe.img_path,
            ingredients: this.recipe.ingredients,
            event_id: this.eventId
        };

        this.dishService
            .post(data)
            .then(recipe => console.log('success'));
    }

}

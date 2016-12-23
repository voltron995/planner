import {Component, Input} from '@angular/core';
import {Recipe} from '../../models/recipe'
import {DishService} from "../../../dishes/services/dish.service";
import {Dish} from "../../../dishes/models/dish";
import {MessageService} from "../../../../../main/services/message.service";
import {ResponseError} from "../../../../../main/models/errors";


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
        private dishSrv: DishService,
        private msgSrv: MessageService,
    ) {}

    createDish() {
        let data = {
            name: this.recipe.name,
            description: this.recipe.description,
            image: this.recipe.image || '',
            ingredients: this.recipe.ingredients.map((value: any) => {
                return {
                    'quantity': value.quantity,
                    'ingredient': {
                        id: value.ingredient.id,
                    }
                }
            }),
            event_id: this.eventId
        };

        this.dishSrv
            .post(data)
            .then((dish: Dish) => {
                this.msgSrv.success(`Dish ${dish.name} successfully added.`);
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}

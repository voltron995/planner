import {Component, Input} from '@angular/core';
import {Recipe} from '../../models/recipe'


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

    constructor() {}


}

import {Component, Input} from '@angular/core';
import {Recipe} from '../../recipes/models/recipe';
import {Dish} from "../../dishes/models/dish";

@Component({
    selector: 'ingredients-list',
    templateUrl: 'ingredients-list.component.html',
    styleUrls: [
        'ingredients-list.component.css'
    ],
})

export class IngredientsListComponent {

    @Input()
    entity: Recipe|Dish;

}

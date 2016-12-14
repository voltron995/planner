import {Component, OnInit,Input} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Recipe} from '../../recipes/models/recipe';

import {Category} from '../../categories/models/category';
import {IngredientService} from "../services/ingredients.service";
import {RecipeService} from "../../recipes/services/recipe.service";
import{Ingredient} from "../models/ingredients";

@Component({
    selector: 'ingredients-list',
    templateUrl: 'ingredients-list.component.html',
    styleUrls: [
        'ingredients-list.component.css'
    ],

})

export class IngredientsListComponent implements OnInit{

    @Input()
    recipe:Recipe;

    ngOnInit(): void {}


  }

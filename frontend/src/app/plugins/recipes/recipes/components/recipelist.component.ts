import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Recipe} from '../models/recipe'
import {RecipeService} from "../services/recipe.service";


@Component({
    selector: 'recipelist',
    templateUrl: 'recipelist.component.html',
    styleUrls: [
        'recipelist.component.css'
    ],

})

export class RecipeListComponent {
    recipes: Recipe[];
    selectedRecipe: Recipe;

    constructor(private recipeService: RecipeService) {
    }

    ngOnInit(): void {
        this.getRecipes();
    }

    getRecipes(): void {
        this.recipeService
        .list()
        .then(recipes => this.recipes = recipes);
    }

    onSelect(recipe: Recipe): void {
        this.selectedRecipe = recipe;
    }
  }

import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";

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

    ingredients: Ingredient[];
    constructor(private ingredientService: IngredientService,
                private recipeService:RecipeService) {
    }

    ngOnInit(): void {
        this.getIngredients();

  }

    getIngredients(): void {
        this.ingredientService
        .list()
        .then(ingredients => this.ingredients = ingredients);
    }

    // onSelect(category: Category): void {
    //     this.selectedCategory = category
    //     this.recipeService
    //     .listCat(this.selectedCategory.id)
    //     .then(recipes => this.recipes = recipes);
    // }
    // onSelected(recipe:Recipe){
    //   this.selectedRecipe = recipe
    //   }
  }

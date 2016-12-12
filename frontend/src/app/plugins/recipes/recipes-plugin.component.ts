import {Component, OnInit, SimpleChanges, OnChanges} from '@angular/core';
import {Category} from "./categories/models/category";
import {Recipe} from "./recipes/models/recipe";

@Component({
    templateUrl: 'recipes-plugin.component.html',
})

export class RecipesPluginComponent {

    selectedCategory: Category;
    selectedRecipe: Recipe;

    constructor() {}

    onCategorySelected(category: Category) {
        console.log(category, 'handleMyEvent');
        this.selectedCategory = category;
    }

    onRecipeSelected(recipe: Recipe) {
        console.log(recipe, 'handleMyRecipe');
        this.selectedRecipe = recipe;
    }

}

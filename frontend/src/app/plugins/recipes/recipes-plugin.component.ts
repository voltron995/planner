import {Component} from '@angular/core';
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
        this.selectedCategory = category;
    }

    onRecipeSelected(recipe: Recipe) {
        this.selectedRecipe = recipe;
    }

}

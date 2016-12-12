import {Component, OnInit, OnDestroy, Input, SimpleChanges, OnChanges} from '@angular/core';
import {Recipe} from '../../models/recipe'
import {RecipeService} from "../../services/recipe.service";
import {Category} from "../../../categories/models/category";


@Component({
    selector: 'recipes',
    templateUrl: 'recipes.component.html',
    styleUrls: [
        'recipes.component.css'
    ],

})

export class RecipesComponent implements OnInit, OnChanges {
    recipes: Recipe[];
    selectedRecipe: Recipe;

    @Input()
    category: Category;

    constructor(
        private recipeService: RecipeService
    ) {}

    ngOnInit(): void {
        console.log('recipes ngOnInit');
        this.getRecipes();
    }

    getRecipes(): void {
        this.recipeService
            .listCat(this.category.id)
            .then(recipes => this.recipes = recipes);
    }

    ngOnChanges(changes: SimpleChanges): void {
        console.log(changes, 'changes');
        this.getRecipes();
    }

    onSelect(recipe: Recipe): void {
        this.selectedRecipe = recipe;
    }
  }

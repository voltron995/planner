import {Component, Output, Input, SimpleChanges, OnChanges, EventEmitter} from '@angular/core';
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

export class RecipesComponent implements OnChanges {
    recipes: Recipe[];

    @Input()
    category: Category;

    @Output()
    onRecipeSelected = new EventEmitter<Category>();

    constructor(
        private recipeSrv: RecipeService
    ) {}

    getRecipes(): void {
        this.recipeSrv
            .listCat(this.category.id)
            .then(recipes => this.recipes = recipes);
    }

    ngOnChanges(changes: SimpleChanges): void {
        this.getRecipes();
    }

    onSelect(recipe: Recipe): void {
           this.onRecipeSelected.next(recipe);
    }
  }

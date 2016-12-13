import {
    Component, OnInit, Output, Input, SimpleChanges, OnChanges, EventEmitter, AfterViewInit,
    ElementRef, ViewChild
} from '@angular/core';
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

    @Input()
    category: Category;

    @Output()
    onRecipeSelected = new EventEmitter<Category>();

    constructor(
        private recipeService: RecipeService
    ) {}

    ngOnInit(): void {
        this.getRecipes();
    }

    getRecipes(): void {
        this.recipeService
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

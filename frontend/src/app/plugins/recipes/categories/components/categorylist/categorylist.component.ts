import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";

import {Category} from '../../models/category';
import {CategoryService} from "../../services/category.service";
import {RecipeService} from "../../../recipes/services/recipe.service";
import{Recipe} from "../../../recipes/models/recipe";

@Component({
    selector: 'categorylist',
    templateUrl: 'categorylist.component.html',
    styleUrls: [
        'categorylist.component.css'
    ],

})

export class CategoryListComponent implements OnInit{

    categories: Category[];
    selectedCategory:Category;
    selectedRecipe:Recipe;
    recipes: Recipe[];
    constructor(private categoryService: CategoryService,
                private recipeService:RecipeService) {
    }

    ngOnInit(): void {
        this.getCategories();

  }

    getCategories(): void {
        this.categoryService
        .list()
        .then(categories => this.categories = categories);
    }

    onSelect(category: Category): void {
        this.selectedCategory = category
        this.recipeService
        .listCat(this.selectedCategory.id)
        .then(recipes => this.recipes = recipes);
    }
    onSelected(recipe:Recipe){
      this.selectedRecipe = recipe
      }
  }

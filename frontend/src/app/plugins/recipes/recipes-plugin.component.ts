import {Component, OnInit, OnDestroy} from '@angular/core';
import {Category} from "./categories/models/category";
import {Recipe} from "./recipes/models/recipe";
import {ActivatedRoute} from "@angular/router";
import {Subscription} from "rxjs";

@Component({
    templateUrl: 'recipes-plugin.component.html',
})

export class RecipesPluginComponent implements OnInit, OnDestroy {

    selectedCategory: Category;
    selectedRecipe: Recipe;

    private params: {
        eventId: string,
    };

    private sub: Subscription;

    constructor(
        private route: ActivatedRoute
    ) {}

    ngOnInit(){
      this.initParams();
    }

    onCategorySelected(category: Category) {
        this.selectedCategory = category;
    }

    onRecipeSelected(recipe: Recipe) {
        this.selectedRecipe = recipe;
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                eventId: params['id'],
            };
        });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }

}

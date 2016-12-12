import {Component, Input, Output, OnInit, OnDestroy, EventEmitter} from '@angular/core';
import {ActivatedRoute} from "@angular/router";

import {Category} from '../../models/category';
import {CategoryService} from "../../services/category.service";
import {RecipeService} from "../../../recipes/services/recipe.service";
import{Recipe} from "../../../recipes/models/recipe";

@Component({
    selector: 'categories',
    templateUrl: 'categories.component.html',
    styleUrls: [
        'categories.component.css'
    ],

})

export class CategoriesComponent {

    categories: Category[];

    @Output()
    onCategorySelected = new EventEmitter<Category>();

    constructor(
        private categoryService: CategoryService,
    ) {}

    ngOnInit(): void {
        this.getCategories();

    }

    getCategories(): void {
        this.categoryService
            .list()
            .then(categories => this.categories = categories);
    }

    onSelect(category: Category): void {
        console.log(category, 'emit');
        this.onCategorySelected.next(category);
    }
}

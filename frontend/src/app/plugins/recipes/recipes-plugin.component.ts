import {Component, OnInit, SimpleChanges, OnChanges} from '@angular/core';
import {Category} from "./categories/models/category";

@Component({
    templateUrl: 'recipes-plugin.component.html',
})

export class RecipesPluginComponent {

    selectedCategory: Category;

    constructor() {}

    onCategorySelected(category: Category) {
        console.log(category, 'handleMyEvent');
        this.selectedCategory = category;
    }

}

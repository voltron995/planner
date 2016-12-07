import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Category} from '../models/category'
import {CategoryService} from "../services/category.service";


@Component({
    selector: 'categorylist',
    templateUrl: 'categorylist.component.html',
    styleUrls: [
        'categorylist.component.css'
    ],

})

export class CategoryListComponent {
    categories: Category[];
    selectedCategory:Category;

    constructor(private categoryService: CategoryService) {
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
        this.selectedCategory = category;
    }
  }

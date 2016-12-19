import {Component, Output, EventEmitter} from '@angular/core';

import {Category} from '../../models/category';
import {CategoryService} from "../../services/category.service";
import {ResponseError} from "../../../../../main/models/errors";
import {MessageService} from "../../../../../main/services/message.service";

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
        private categorySrv: CategoryService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initCategories();
    }

    initCategories(): void {
        this.categorySrv
            .list()
            .then(categories => this.categories = categories)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    onSelect(category: Category): void {
        this.onCategorySelected.next(category);
    }

}

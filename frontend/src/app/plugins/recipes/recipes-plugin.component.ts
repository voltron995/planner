import {Component} from '@angular/core';

@Component({
    templateUrl: 'recipes-plugin.component.html',
})


export class PluginComponent  {

export class RecipesPluginComponent implements OnInit {

    categories: Array<any>;

    constructor() {
    }

    ngOnInit() {
        this.initCategories();
    }

    protected initCategories() {
        this.categories = [1, 2, 3, 4, 5];
    }

}

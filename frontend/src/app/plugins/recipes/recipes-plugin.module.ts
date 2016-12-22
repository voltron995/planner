import {NgModule} from '@angular/core';
import {SelectModule} from 'angular2-select';
import {DishService} from "./dishes/services/dish.service";
import {IngredientService} from "./ingredients/services/ingredients.service";
import {IngredientsListComponent} from "./ingredients/components/ingredients-list.component";
import {RecipesPluginComponent} from "./recipes-plugin.component";
import {CategoryService} from "./categories/services/category.service";
import {RecipeService} from "./recipes/services/recipe.service";
import {CategoriesComponent} from "./categories/components/categories/categories.component";
import {RecipesComponent} from "./recipes/components/recipes/recipes.component";
import {RecipeComponent} from "./recipes/components/recipe/recipe.component";
import {MasonryModule} from "angular2-masonry/src/module";
import {RouterModule} from "@angular/router";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {CommonModule} from "@angular/common";
import {FileUploadModule} from "ng2-file-upload";
import {DishEditComponent} from "./dishes/components/dish-edit/dish-edit.component";
import {DishEditForm} from "./dishes/forms/dish-edit/dish-edit.form";
import {DishComponent} from "./dishes/components/dish/dish.component";

@NgModule({
    imports: [
        CommonModule,
        SelectModule,
        FileUploadModule,
        FormsModule,
        MasonryModule,
        ReactiveFormsModule,
        RouterModule.forChild([
            {
                path: '',
                component: RecipesPluginComponent,
            },
            {
                path: 'dishes',
                children: [
                    {
                        path: ':dish_id',
                        children: [
                            {
                                path: '',
                                component: DishComponent,
                            },
                            {
                                path: 'edit',
                                component: DishEditComponent,
                            }
                        ]
                    }
                ]
            }
        ]),
    ],
    declarations: [
        RecipesPluginComponent,
        IngredientsListComponent,
        CategoriesComponent,
        RecipeComponent,
        RecipesComponent,
        DishComponent,
        DishEditComponent,
        DishEditForm,
    ],
    providers: [
        DishService,
        CategoryService,
        RecipeService,
        IngredientService
    ]
})
export class RecipesPluginModule {
}

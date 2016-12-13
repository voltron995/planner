import {Component, Input,OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Recipe} from '../../models/recipe'
import {RecipeService} from "../../services/recipe.service";
import {Ingredient} from "../../../ingredients/models/ingredients";
import {IngredientService} from "../../../ingredients/services/ingredients.service";



@Component({
    selector: 'recipe-detail',
    templateUrl: 'recipe-detail.component.html',
    styleUrls: [
        'recipe-detail.component.css'
    ],

})

export class RecipeDetailComponent {
  @Input() selectedRecipe:Recipe;
  ingredients:Ingredient[];



constructor(private recipeService:RecipeService,
            private ingrService:IngredientService,
){}
//i dont know how recived list of recipe ingredient
//getIngredients(): {
    // this.ingrService
    // for (let i=0; i<this.selectedRecipe.ingredients.length; i++){
    //   console.log(this.selectedRecipe.ingredients[i].name)
    //   return this.selectedRecipe.ingredients[i].name
    //   console.log(this.selectedRecipe.ingredients[i].name)
    // }

}

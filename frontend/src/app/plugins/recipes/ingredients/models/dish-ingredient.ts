import {Ingredient} from "./ingredients";

export class DishIngredient {

    quantity: number;
    ingredient: Ingredient;

    constructor(quantity: number, ingredient: Ingredient) {
        this.quantity = quantity;
        this.ingredient = ingredient;
    }

    public static newFromResponse(data: any) {
        return new this(data.quantity, Ingredient.newFromResponse(data.ingredient));
    }

}

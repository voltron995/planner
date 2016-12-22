import {Ingredient} from "../../ingredients/models/ingredients";

export class Recipe {

    public id: string;
    public name: string;
    public description: string;
    public price: string;
    public image: string;
    public imageLink: string;
    public ingredients: Ingredient[];

    constructor(id: string, attributes: any) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.price = attributes.price;
        this.ingredients = attributes.ingredients;
        this.image = attributes.image;
        this.imageLink = attributes.imageLink;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            price: data.price,
            ingredients: data.ingredients,
            image: data.image,
            imageLink: data.image_link,
        });
    }

}

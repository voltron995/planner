import {Ingredient} from "../../ingredients/models/ingredients";
export class Dish {

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
        this.image = attributes.image;
        this.imageLink = attributes.imageLink;
        this.ingredients = [];
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            price: data.price,
            image: data.img_path,
            imageLink: data.image_link,
        });
    }

}

export class Recipe {

    public id: string;
    public name: string;
    public description: string;
    public price: string;

    constructor(id: string, attributes: any) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.price = attributes.price;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            price: data.price,
        });
    }

  }
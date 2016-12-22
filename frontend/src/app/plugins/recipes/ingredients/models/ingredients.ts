export class Ingredient{

    public id: string;
    public name: string;
    public description: string;
    public img_path: string;
    public dimension: string;

    constructor(id: string, attributes: any) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.img_path = attributes.img_path;
        this.dimension = attributes.dimension
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name,
            description:data.description,
            img_path:data.img_path,
            dimension:data.dimension

          });
    }

}

export class Category {

    public id: string;
    public name: string;


    constructor(id: string, attributes: any) {
        this.id = id;
        this.name = attributes.name;

    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name
          });
    }

}

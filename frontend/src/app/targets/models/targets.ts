export class Target {

    public id: string;
    public name: string;
    public description: string;
    public is_done: boolean;
    public target_id: string;

    constructor(
        id: string,
        attributes: any
    ) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.is_done = attributes.is_done;
        this.target_id = attributes.target_id;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            is_done: data.is_done,
            target_id: data.target_id,
        });
    }

}

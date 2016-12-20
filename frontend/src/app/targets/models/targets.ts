export class Target {

    public id: string;
    public name: string;
    public description: string;
    public is_done: boolean;
    public targets: Array<any>;

    constructor(
        id: string,
        attributes: any
    ) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.is_done = attributes.is_done;
        this.targets = attributes.targets;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            is_done: data.is_done,
            targets: data.targets,
        });
    }

}

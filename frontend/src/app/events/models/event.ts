export class Event {

    public id: string;
    public name: string;
    public description: string;
    public startTime: string;
    public endTime: string;
    public colorPrimary: string;
    public colorSecondary: string;
    public isDone: boolean;
    public items: Array<any>;

    constructor(
        id: string,
        attributes: any
    ) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.startTime = attributes.startTime;
        this.endTime = attributes.endTime;
        this.colorPrimary = attributes.colorPrimary;
        this.colorSecondary = attributes.colorSecondary;
        this.isDone = attributes.isDone;
        this.items = attributes.items;
    }

    public static newFromResponseData(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            startTime: data.start_time,
            endTime: data.end_time,
            colorPrimary: data.color_primary,
            colorSecondary: data.color_secondary,
            isDone: data.is_done,
            items: data.items,
        });
    }

}

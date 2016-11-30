export class Event {

    public id: string;
    public name: string;
    public description: string;
    public startTime: string;
    public endTime: string;
    public isDone: boolean;

    constructor(
        id: string,
        attributes: any
    ) {
        this.id = id;
        this.name = attributes.name;
        this.description = attributes.description;
        this.startTime = attributes.startTime;
        this.endTime = attributes.endTime;
        this.isDone = attributes.isDone;
    }

    public static newFromResponseData(data: any) {
        return new this(data.id, {
            name: data.name,
            description: data.description,
            startTime: data.start_time,
            endTime: data.end_time,
            isDone: data.is_done,
        });
    }

}

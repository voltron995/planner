export class Event {

    public uuid: string;
    public name: string;
    public description: string;
    public startTime: string;
    public endTime: string;
    public isDone: boolean;

    constructor(
        uuid: string,
        attributes: any
    ) {
        this.uuid = uuid;
        this.name = attributes.name;
        this.description = attributes.description;
        this.startTime = attributes.startTime;
        this.endTime = attributes.endTime;
        this.isDone = attributes.isDone;
    }

    public static newFromResponseData(data: any) {
        return new this(data.uuid, {
            name: data.attributes.name,
            description: data.attributes.description,
            startTime: data.attributes.start_time,
            endTime: data.attributes.end_time,
            isDone: data.attributes.is_done,
        });
    }

}

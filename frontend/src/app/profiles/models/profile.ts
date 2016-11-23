export class Profile {

    public uuid: string;
    public firstName: string;
    public lastName: string;
    public birthDate: string;
    public image: string;
    public imageLink: string;

    constructor(
        uuid: string,
        attributes: any
    ) {
        this.uuid = uuid;
        this.firstName = attributes.firstName;
        this.lastName = attributes.lastName;
        this.birthDate = attributes.birthDate;
        this.image = attributes.image;
        this.imageLink = attributes.imageLink;
    }

    public static newFromResponseData(data: any) {
        return new this(data.uuid, {
            firstName: data.attributes.first_name,
            lastName: data.attributes.last_name,
            birthDate: data.attributes.birth_date,
            image: data.attributes.image,
            imageLink: data.attributes.image_link,
        });
    }

}

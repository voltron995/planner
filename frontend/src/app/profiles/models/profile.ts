export class Profile {

    public id: string;
    public firstName: string;
    public lastName: string;
    public birthDate: string;
    public image: string;
    public imageLink: string;

    constructor(
        id: string,
        attributes: any
    ) {
        this.id = id;
        this.firstName = attributes.firstName;
        this.lastName = attributes.lastName;
        this.birthDate = attributes.birthDate;
        this.image = attributes.image;
        this.imageLink = attributes.imageLink;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            firstName: data.first_name,
            lastName: data.last_name,
            birthDate: data.birth_date,
            image: data.image,
            imageLink: data.image_link,
        });
    }

}

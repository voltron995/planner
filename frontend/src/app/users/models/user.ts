import {Profile} from '../../profiles/models/profile';

export class User {

    public uuid: string;
    public email: string;
    public login: string;
    public profile: Profile;

    constructor(
        uuid: string,
        attributes: any
    ) {
        this.uuid = uuid;
        this.email = attributes.email;
        this.login = attributes.login;
        this.profile = attributes.profile;
    }

    public static newFromResponseData(data: any) {
        return new this(data.uuid, {
            email: data.attributes.email,
            login: data.attributes.login,
            profile: Profile.newFromResponseData(data.attributes.profile)
        });
    }

}

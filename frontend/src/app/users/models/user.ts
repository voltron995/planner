import {Profile} from '../../profiles/models/profile';

export class User {

    public id: string;
    public email: string;
    public login: string;
    public profile: Profile;

    constructor(
        id: string,
        attributes: any
    ) {
        this.id = id;
        this.email = attributes.email;
        this.login = attributes.login;
        this.profile = attributes.profile;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            email: data.email,
            login: data.login,
            profile: Profile.newFromResponse(data.profile)
        });
    }

}

import {Profile} from './profile';

export class User {

    constructor(
        public id: number,
        public email: string,
        public login: string,
        public profile?: Profile
    ) {}

}

import {Injectable} from '@angular/core';

import {User} from '../models/user'
import {RequestService} from '../../main/services/request.service';


@Injectable()
export class UserService {

    private usersUrl = 'api/v1.0/users';

    constructor(
        private requestSrv: RequestService,
    ) {}

    getCurrent(): Promise<User> {
        const url = `${this.usersUrl}/current`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(User.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }


    putCurrent(data: any): Promise<User> {
        const url = `${this.usersUrl}/current`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .put(url, data)
                .then(response => resolve(User.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }
}
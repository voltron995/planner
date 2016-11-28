import {Injectable} from '@angular/core';
import {Headers} from '@angular/http';

import 'rxjs/add/operator/toPromise';

import {User} from '../models/user'
import {RequestService} from '../../main/services/request.service';
import {ResponseService} from '../../main/services/response.service';

@Injectable()
export class UserService {

    private headers = new Headers({'Content-Type': 'application/json'});

    private type = 'users';

    private usersUrl = 'api/v1.0/users';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    getCurrent(): Promise<User> {
        const url = `${this.usersUrl}/current`;

        return this.requestSrv
            .get(url)
            .then(response => User.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }


    putCurrent(data: any): Promise<User> {
        const url = `${this.usersUrl}/current`;

        return this.requestSrv
            .put(url, data)
            .then(response => User.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }
}
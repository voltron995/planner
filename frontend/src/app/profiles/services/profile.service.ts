import {Injectable} from '@angular/core';
import 'rxjs/add/operator/toPromise';

import {Profile} from '../models/profile'
import {RequestService} from '../../main/services/request.service';
import {ResponseService} from '../../main/services/response.service';



@Injectable()
export class ProfileService {

    private type = 'profiles';

    private profilesUrl = 'api/v1.0/profiles';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    getCurrent(): Promise<Profile> {
        const url = `${this.profilesUrl}/current`;

        return this.requestSrv
            .get(url)
            .then(response => Profile.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    putCurrent(uuid: string, attrs: any): Promise<Profile> {
        const url = `${this.profilesUrl}/current`;

        return this.requestSrv
            .put(url, this.type, uuid, attrs)
            .then(response => Profile.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

}
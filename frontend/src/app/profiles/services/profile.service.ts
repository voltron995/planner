import {Injectable} from '@angular/core';

import {Profile} from '../models/profile'
import {RequestService} from '../../main/services/request.service';


@Injectable()
export class ProfileService {

    private profilesUrl = 'api/v1.0/profiles';

    constructor(
        private requestSrv: RequestService
    ) {}

    putCurrent(data: any): Promise<Profile> {
        const url = `${this.profilesUrl}/current`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .put(url, data)
                .then(response => resolve(Profile.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

}
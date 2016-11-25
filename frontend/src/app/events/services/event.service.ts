import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {Event} from '../models/event'
import {RequestService} from "../../main/services/request.service";
import {ResponseService} from "../../main/services/response.service";


@Injectable()
export class EventService {

    private eventsUrl = 'api/v1.0/events';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    list(): Promise<Event[]> {
        return this.requestSrv
            .get(this.eventsUrl)
            // .then(response => this.responseSrv.parseData(response))
            .then(response => this.responseSrv.parseData(response).map((item: any) => Event.newFromResponseData(item)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

}
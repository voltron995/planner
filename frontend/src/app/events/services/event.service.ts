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

    get(id: string): Promise<Event> {
        const url = `${this.eventsUrl}/${id}`;

        return this.requestSrv
            .get(url)
            .then(response => Event.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    put(id: string, data: any): Promise<Event> {
        const url = `${this.eventsUrl}/${id}`;

        return this.requestSrv
            .put(url, data)
            .then(response => Event.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    post(data: any): Promise<Event> {
        const url = `${this.eventsUrl}/`;

        return this.requestSrv
            .post(url, data)
            .then(response => Event.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    delete(id: string): Promise<Event> {
        const url = `${this.eventsUrl}/${id}`;

        return this.requestSrv
            .delete(url)
            .then(response => this.responseSrv.parseData(response))
            .catch(response => this.responseSrv.parseErrors(response));
    }

}
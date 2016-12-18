import {Injectable} from '@angular/core';

import {Event} from '../models/event'
import {RequestService} from "../../main/services/request.service";


@Injectable()
export class EventService {

    private eventsUrl = 'api/v1.0/events';

    constructor(
        private requestSrv: RequestService,
    ) {}

    list(): Promise<Event[]> {
        const url = `${this.eventsUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(response.map((item: any) => Event.newFromResponse(item))))
                .catch(errors => reject(errors));
        });
    }

    get(id: string): Promise<Event> {
        const url = `${this.eventsUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(Event.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    put(id: string, data: any): Promise<Event> {
        const url = `${this.eventsUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .put(url, data)
                .then(response => resolve(Event.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    post(data: any): Promise<Event> {
        const url = `${this.eventsUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .post(url, data)
                .then(response => resolve(Event.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    delete(id: string): Promise<Event> {
        const url = `${this.eventsUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .delete(url)
                .then(response => resolve(response))
                .catch(errors => reject(errors));
        });
    }

}
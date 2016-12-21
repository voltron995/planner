import {Injectable} from '@angular/core'

import {Target} from '../models/targets'
import {RequestService} from "../../main/services/request.service";

@Injectable()
export class TargetService {

    private targetUrl = 'api/v1.0/targets';

    constructor(
        private  requestSrv: RequestService,
    ) {}

    list(): Promise<Target[]> {
        const url = `${this.targetUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(response.map((item: any) => Target.newFromResponse(item))))
                .catch(errors => reject(errors));
        });
    }

    get(id: string): Promise<Target> {
        const url = `${this.targetUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(Target.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    put(id: string, data: any): Promise<Target> {
        const url = `${this.targetUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .put(url, data)
                .then(response => resolve(Target.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    post(data: any): Promise<Target> {
        const url = `${this.targetUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .post(url, data)
                .then(response => resolve(Target.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    delete(id: string): Promise<Target> {
        const url = `${this.targetUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .delete(url)
                .then(response => resolve(response))
                .catch(errors => reject(errors));
        });
    }
}


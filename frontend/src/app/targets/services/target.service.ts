import {Injectable} from '@angular/core'
import 'rxjs/add/operator/toPromise';

import {Target} from '../models/targets'
import {RequestService} from "../../main/services/request.service";
import {ResponseService} from "../../main/services/response.service";

@Injectable()
export class TargetService {

    private targetUrl = 'api/v1.0/targets';

    constructor(
        private  requestSrv: RequestService,
        private  responseSrv: ResponseService
    ) {}

    list(): Promise<Target[]> {
        return this.requestSrv
            .get(this.targetUrl)
            .then((response: any) => this.responseSrv.parseData(response).map((target: any) => Target.newFromResponseData(target)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    get(id: string): Promise<Target> {
        const url = `${this.targetUrl}/${id}`;

        return this.requestSrv
            .get(url)
            .then(response => Target.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    put(id: string, data: any): Promise<Target> {
        const url = `${this.targetUrl}/${id}`;

        return this.requestSrv
            .put(url, data)
            .then(response => Target.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    post(data: any): Promise<Target> {
        const url = `${this.targetUrl}/`;

        return this.requestSrv
            .post(url, data)
            .then(response => Target.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));

    }

    delete(id: string): Promise<Target> {
        const url = `${this.targetUrl}/${id}`;

        return this.requestSrv
            .delete(url)
            .then(response => Target.newFromResponseData(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));

    }
}


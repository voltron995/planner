import {Injectable} from '@angular/core';
import {Http, Headers, URLSearchParams} from '@angular/http';

import 'rxjs/add/operator/toPromise';
import {ResponseService} from "./response.service";


@Injectable()
export class RequestService {

    private headers = new Headers({'Content-Type': 'application/json'});

    constructor(
        private http: Http,
        private responseSrv: ResponseService
    ) {}

    get(url: string, params?: URLSearchParams): Promise<any> {
        return new Promise((resolve, reject) => {
            this.http
                .get(url, {search: params})
                .toPromise()
                .then(response => resolve(this.responseSrv.parseData(response)))
                .catch(errors => reject(this.responseSrv.parseErrors(errors)));
        });
    }

    put(url: string, data: any): Promise<any> {
        return new Promise((resolve, reject) => {
            this.http
                .put(url, data, {headers: this.headers})
                .toPromise()
                .then(response => resolve(this.responseSrv.parseData(response)))
                .catch(errors => reject(this.responseSrv.parseErrors(errors)));
        });
    }

    post(url: string, data: any): Promise<any> {
        return new Promise((resolve, reject) => {
            this.http
                .post(url, data, {headers: this.headers})
                .toPromise()
                .then(response => resolve(this.responseSrv.parseData(response)))
                .catch(errors => reject(this.responseSrv.parseErrors(errors)));
        });
    }

    delete(url: string, params?: URLSearchParams): Promise<any> {
        return new Promise((resolve, reject) => {
            this.http
                .delete(url, {search: params})
                .toPromise()
                .then(response => resolve(this.responseSrv.parseData(response)))
                .catch(errors => reject(this.responseSrv.parseErrors(errors)));
        });
    }

}
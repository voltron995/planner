import {Injectable} from '@angular/core';
import {Http, Headers, URLSearchParams} from '@angular/http';

import 'rxjs/add/operator/toPromise';


@Injectable()
export class RequestService {

    private headers = new Headers({'Content-Type': 'application/json'});

    constructor(private http: Http) {}

    get(url: string, params?: URLSearchParams): Promise<any> {
        return this.http
            .get(url, {search: params})
            .toPromise()
    }

    put(url: string, type: string, uuid: string, attributes: any): Promise<any> {
        let body = {
            data: {
                uuid: uuid,
                type: type,
                attributes: attributes
            }
        };
        return this.http
            .put(url, body, {headers: this.headers})
            .toPromise();
    }



}
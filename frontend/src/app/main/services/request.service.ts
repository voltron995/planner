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

    delete(url: string): Promise<any> {
        return this.http.delete(url, {headers: this.headers})
            .toPromise();
    }

    put(url: string, data: any): Promise<any> {
        return this.http
            .put(url, data, {headers: this.headers})
            .toPromise();
    }

    post(url: string, data: any): Promise<any> {
        return this.http
            .post(url, data, {headers: this.headers})
            .toPromise();
    }


}
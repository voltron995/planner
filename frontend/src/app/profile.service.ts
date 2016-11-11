import {Injectable} from '@angular/core';
import {Http, Headers} from '@angular/http';

import 'rxjs/add/operator/toPromise';

import {Profile} from './profile'


@Injectable()
export class ProfileService {

    private headers = new Headers({'Content-Type': 'application/json'});

    private eventsUrl = 'api/profiles';

    constructor(private http: Http) {
    }

    get(id: number): Promise<Profile> {
        const url = `${this.eventsUrl}/${id}`;

        // return this.http.get(url, {
        //     headers: this.headers
        // })
        // .toPromise()
        // .then((response => response.json().data as Profile) => null)
        // .catch(this.handleError);
    }

    delete(id: number): Promise<void> {
        const url = `${this.heroesUrl}/${id}`;
        return this.http.delete(url, {headers: this.headers})
        .toPromise()
        .then(() => null)
        .catch(this.handleError);
    }

    getProfiles(): Promise<Event[]> {
        return this.http.get(this.eventsUrl)
            .toPromise()
            .then(response => response.json().data as Event[])
            .catch(this.handleError)
    }

    private handleError(error: any): Promise<any> {
        console.error('An error occurred', error); // for demo purposes only
        return Promise.reject(error.message || error);
    }

}
import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../../../main/services/request.service";
import {ResponseService} from "../../../../main/services/response.service";
import {Dish} from "../models/dish";
import {URLSearchParams} from "@angular/http";


@Injectable()
export class DishService {

    private dishUrl = 'api/v1.0/plugins/recipes/dishes';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    get(id: string): Promise<Dish> {
        const url = `${this.dishUrl}/${id}`;

        return this.requestSrv
            .get(url)
            .then(response => Dish.newFromResponse(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
     }

    list(): Promise<Dish[]> {
        const url = `${this.dishUrl}/`;

        return this.requestSrv
            .get(url)
            .then(response => this.responseSrv.parseData(response).map((item: any) => Dish.newFromResponse(item)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    put(id: string, data: any): Promise<Dish> {
        const url = `${this.dishUrl}/${id}`;

        return this.requestSrv
            .put(url, data)
            .then(response => Dish.newFromResponse(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

    post(data: any): Promise<Dish> {
        const url = `${this.dishUrl}/`;

        return this.requestSrv
            .post(url, data)
            .then(response => Dish.newFromResponse(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
    }



}

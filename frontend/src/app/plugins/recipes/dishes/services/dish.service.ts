import {Injectable} from '@angular/core';

import {RequestService} from "../../../../main/services/request.service";
import {Dish} from "../models/dish";


@Injectable()
export class DishService {

    private dishUrl = 'api/v1.0/plugins/recipes/dishes';

    constructor(
        private requestSrv: RequestService,
    ) {}

    list(): Promise<Dish[]> {
        const url = `${this.dishUrl}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(response.map((item: any) => Dish.newFromResponse(item))))
                .catch(errors => reject(errors));
        });
    }

    get(id: string): Promise<Dish> {
        const url = `${this.dishUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(Dish.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    put(id: string, data: any): Promise<Dish> {
        const url = `${this.dishUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .put(url, data)
                .then(response => resolve(Dish.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    post(data: any): Promise<Dish> {
        const url = `${this.dishUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .post(url, data)
                .then(response => resolve(Dish.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    delete(id: string): Promise<any> {
        const url = `${this.dishUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .delete(url)
                .then(response => resolve(response))
                .catch(errors => reject(errors));
        });
    }

}

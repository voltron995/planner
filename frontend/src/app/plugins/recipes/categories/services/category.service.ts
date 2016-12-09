import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../../../main/services/request.service";
import {ResponseService} from "../../../../main/services/response.service";
import {Category} from "../models/category";
import {URLSearchParams} from "@angular/http";


@Injectable()
export class CategoryService {

    private categoryUrl = 'api/v1.0/plugins/recipes/recipes/categories';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    list(): Promise<Category[]> {
        return this.requestSrv
            .get(this.categoryUrl)
            .then(response => this.responseSrv.parseData(response).map((item: any) => Category.newFromResponse(item)))
            .catch(response => this.responseSrv.parseErrors(response));
    }
    get(id: string): Promise<Category> {
        const url = `${this.categoryUrl}/${id}`;

        return this.requestSrv
            .get(url)
            .then(response => Category.newFromResponse(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
     }


    // put(id: string, data: any): Promise<Category> {
    //     const url = `${this.dishUrl}/${id}`;
    //
    //     return this.requestSrv
    //         .put(url, data)
    //         .then(response => Dish.newFromResponse(this.responseSrv.parseData(response)))
    //         .catch(response => this.responseSrv.parseErrors(response));
    // }
    //
    // post(data: any): Promise<Dish> {
    //     return this.requestSrv
    //         .post(this.dishUrl, data)
    //         .then(response => Dish.newFromResponse(this.responseSrv.parseData(response)))
    //         .catch(response => this.responseSrv.parseErrors(response));
    // }



}

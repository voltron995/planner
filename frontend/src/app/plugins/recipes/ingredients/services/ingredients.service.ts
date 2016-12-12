import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../../../main/services/request.service";
import {ResponseService} from "../../../../main/services/response.service";
import {Ingredient} from "../models/ingredients";
import {URLSearchParams} from "@angular/http";


@Injectable()
export class IngredientService {

    private ingredientUrl = 'api/v1.0/plugins/recipes/ingredients';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    list(): Promise<Ingredient[]> {
        return this.requestSrv
            .get(this.ingredientUrl)
            .then(response => this.responseSrv.parseData(response).map((item: any) => Ingredient.newFromResponse(item)))
            .catch(response => this.responseSrv.parseErrors(response));
    }
    get(id: string): Promise<Ingredient> {
        const url = `${this.ingredientUrl}/${id}`;

        return this.requestSrv
            .get(url)
            .then(response => Ingredient.newFromResponse(this.responseSrv.parseData(response)))
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

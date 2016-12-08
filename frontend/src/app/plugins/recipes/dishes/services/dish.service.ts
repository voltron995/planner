import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../../../main/services/request.service";
import {ResponseService} from "../../../../main/services/response.service";
import {Dish} from "../models/dish";


@Injectable()
export class DishService {

    private dishUrl = 'api/v1.0/plugins/recipes/dishes/';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    list(): Promise<Dish[]> {
        return this.requestSrv
            .get(this.dishUrl)
            .then(response => this.responseSrv.parseData(response).map((item: any) => Dish.newFromResponse(item)))
            .catch(response => this.responseSrv.parseErrors(response));
    }

}
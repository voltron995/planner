import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../../../main/services/request.service";
import {ResponseService} from "../../../../main/services/response.service";
import {Recipe} from "../models/recipe";


@Injectable()
export class RecipeService {

    private recipeUrl = 'api/v1.0/plugins/recipes/recipes/';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}

    list(): Promise<Recipe[]> {
        return this.requestSrv
            .get(this.recipeUrl)
            .then(response => this.responseSrv.parseData(response).map((item: any) => Recipe.newFromResponse(item)))
            .catch(response => this.responseSrv.parseErrors(response));
    }
    get(id: string): Promise<Recipe> {
        const url = `${this.recipeUrl}/${id}`;

        return this.requestSrv
            .get(url)
            .then(response => Recipe.newFromResponse(this.responseSrv.parseData(response)))
            .catch(response => this.responseSrv.parseErrors(response));
     }


}

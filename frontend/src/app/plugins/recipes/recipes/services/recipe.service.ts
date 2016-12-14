import {Injectable} from '@angular/core';
import {URLSearchParams } from '@angular/http';
import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../../../main/services/request.service";
import {ResponseService} from "../../../../main/services/response.service";
import {Recipe} from "../models/recipe";


@Injectable()
export class RecipeService {


    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}
    private recipeUrl = 'api/v1.0/plugins/recipes/recipes';
    private dishUrl = 'api/v1.0/plugins/recipes/dishes';
    // getRecipe(id: string):Promise<Recipe[]> {
    //   let params = new URLSearchParams();
    //   params.set('categories',id)
    //
    //   return this.requestSrv
    //         .get(this.recipeUrl + {search:params})
    //         .then(response => this.responseSrv.parseData(response).map((item:any) => Recipe.newFromResponse(item)))
    //         .catch(response => this.responseSrv.parseErrors(response));

    //}
    listCat(id:string): Promise<Recipe[]> {
        let params = new URLSearchParams();
        params.set('categories',id);
        return this.requestSrv
            .get(this.recipeUrl, params)
            // .then(response => this.responseSrv.parseData(response).map((item: any) => Recipe.newFromResponse(item)))
            // todo: this is only for development purposes and should be removed!
            .then(response => {
                // Display more recipes than we really have.
                let x = this.responseSrv.parseData(response).map((item: any) => Recipe.newFromResponse(item));
                return x.concat(x, x, x, x, x, x);
            })
            .catch(response => this.responseSrv.parseErrors(response));
    }
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
     post(data: any): Promise<Recipe> {
         const url = `${this.recipeUrl}`;

         return this.requestSrv
             .post(url, data)
             .then(response => Recipe.newFromResponse(this.responseSrv.parseData(response)))
             .catch(response => this.responseSrv.parseErrors(response));
     }
     postDish(data: any): Promise<Recipe> {
         const url = `${this.dishUrl}`;

         return this.requestSrv
             .post(url, data)
             .then(response => Recipe.newFromResponse(this.responseSrv.parseData(response)))
             .catch(response => this.responseSrv.parseErrors(response));
     }


}

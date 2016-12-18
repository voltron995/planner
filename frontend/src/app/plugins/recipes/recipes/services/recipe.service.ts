import {Injectable} from '@angular/core';
import {URLSearchParams} from '@angular/http';

import {RequestService} from "../../../../main/services/request.service";
import {Recipe} from "../models/recipe";


@Injectable()
export class RecipeService {

    constructor(
        private requestSrv: RequestService,
    ){}

    private recipeUrl = 'api/v1.0/plugins/recipes/recipes';

    listCat(id: string): Promise<Recipe[]> {
        const url = `${this.recipeUrl}/`;

        let params = new URLSearchParams();
        params.set('categories', id);

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url, params)
                // .then(response => resolve(response.map((item: any) => Recipe.newFromResponse(item))))
                // todo: this is only for development purposes and should be removed!
                .then(response => {
                    // Display more recipes than we really have.
                    let x = response.map((item: any) => Recipe.newFromResponse(item));
                    return resolve(x.concat(x, x, x, x, x, x));
                })
                .catch(errors => reject(errors));
        });
    }

    list(): Promise<Recipe[]> {
        const url = `${this.recipeUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(response.map((item: any) => Recipe.newFromResponse(item))))
                .catch(errors => reject(errors));
        });

    }

    get(id: string): Promise<Recipe> {
        const url = `${this.recipeUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(Recipe.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }

    post(data: any): Promise<Recipe> {
        const url = `${this.recipeUrl}/`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url, data)
                .then(response => resolve(Recipe.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }
}

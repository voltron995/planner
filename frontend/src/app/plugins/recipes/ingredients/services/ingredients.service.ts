import {Injectable} from '@angular/core';

import {RequestService} from "../../../../main/services/request.service";
import {Ingredient} from "../models/ingredients";


@Injectable()
export class IngredientService {

    private ingredientUrl = 'api/v1.0/plugins/recipes/ingredients';

    constructor(
        private requestSrv: RequestService,
    ) {}

    list(): Promise<Ingredient[]> {
        const url = `${this.ingredientUrl}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(response.map((item: any) => Ingredient.newFromResponse(item))))
                .catch(errors => reject(errors));
        });
    }

    get(id: string): Promise<Ingredient> {
        const url = `${this.ingredientUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(Ingredient.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }
}

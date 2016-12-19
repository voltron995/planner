import {Injectable} from '@angular/core';

import {RequestService} from "../../../../main/services/request.service";
import {Category} from "../models/category";


@Injectable()
export class CategoryService {

    private categoryUrl = 'api/v1.0/plugins/recipes/recipes/categories';

    constructor(
        private requestSrv: RequestService,
    ) {}

    list(): Promise<Category[]> {
        const url = `${this.categoryUrl}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                // .then(response => resolve(response.map((item: any) => Category.newFromResponse(item))))
                // todo: this is only for development purposes and should be removed!
                .then(response => {
                    // Display more categories than we really have.
                    let x = response.map((item: any) => Category.newFromResponse(item));
                    return resolve(x.concat(x, x, x, x, x, x));
                })
                .catch(errors => reject(errors));
        });
    }

    get(id: string): Promise<Category> {
        const url = `${this.categoryUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .then(response => resolve(Category.newFromResponse(response)))
                .catch(errors => reject(errors));
        });
    }
}

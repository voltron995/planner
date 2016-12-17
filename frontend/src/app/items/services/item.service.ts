import {Injectable} from '@angular/core';

import 'rxjs/add/operator/toPromise';

import {RequestService} from "../../main/services/request.service";
import {ResponseService} from "../../main/services/response.service";
import {BasePlugin} from "../../plugins/base-plugin";
import {PluginItem} from "../../plugins/plugin-item";
import {Item} from "../models/item";


@Injectable()
export class ItemService {

    private itemsUrl = 'api/v1.0';

    constructor(
        private requestSrv: RequestService,
        private responseSrv: ResponseService
    ) {}


    get(item: Item, plugin: BasePlugin): any {
        const url = `${this.itemsUrl}/plugins/${plugin.slug}/${plugin.itemUrl}/${item.pluginItemId}`;

        return this.requestSrv
            .get(url)
            .then(response => {
                response = this.responseSrv.parseData(response);
                return new plugin.itemClass(item.id, {
                    pluginId: response.id,
                    plugin: plugin.slug,
                    name: response.name,
                    image: response.image
                });
            })
            .catch(response => this.responseSrv.parseErrors(response));
    }

    delete(id: string) {
        const url = `${this.itemsUrl}/items/${id}`;

        return this.requestSrv
            .delete(url)
            .then(response => this.responseSrv.parseData(response))
            .catch(errors => this.responseSrv.parseErrors(errors));
    }

}
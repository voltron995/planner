import {Injectable} from '@angular/core';

import {RequestService} from "../../main/services/request.service";
import {BasePlugin} from "../../plugins/base-plugin";
import {Item} from "../models/item";


@Injectable()
export class ItemService {

    private itemsUrl = 'api/v1.0';

    constructor(
        private requestSrv: RequestService,
    ) {}

    get(item: Item, plugin: BasePlugin): any {
        const url = `${this.itemsUrl}/plugins/${plugin.slug}/${plugin.itemUrl}/${item.pluginItemId}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .get(url)
                .catch(errors => reject(errors))
                .then(response => resolve(
                    new plugin.itemClass(item.id, {
                        pluginId: response.id,
                        plugin: plugin.slug,
                        name: response.name,
                        image: response.image_link
                    }))
                );
        });
    }

    delete(id: string, plugin: BasePlugin): any {
        const url = `${this.itemsUrl}/plugins/${plugin.slug}/${plugin.itemUrl}/${id}`;

        return new Promise((resolve, reject) => {
            this.requestSrv
                .delete(url)
                .then(response => resolve(response))
                .catch(errors => reject(errors));
        });
    }
}
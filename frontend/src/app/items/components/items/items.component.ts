import {Component, Input} from '@angular/core';
import {OnInit} from '@angular/core';
import {Event} from "../../../events/models/event";
import {ItemService} from "../../services/item.service";
import {PluginsFactory} from "../../../plugins/plugins-factory";
import {PluginItem} from "../../../plugins/plugin-item";
import {Router, ActivatedRoute} from "@angular/router";
import {MessageService} from "../../../main/services/message.service";
import {ResponseError} from "../../../main/models/errors";


@Component({
    selector: 'items',
    templateUrl: 'items.component.html',
    styleUrls: [
        'items.component.css'
    ]
})

export class ItemsComponent implements OnInit {

    @Input()
    event: Event;

    items: PluginItem[];

    constructor(
        private itemSrv: ItemService,
        private route: ActivatedRoute,
        private router: Router,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initPluginItems();
    }

    initPluginItems() {
        this.items = [];
        this.event.items.map(item => {
            this.itemSrv
                .get(item, PluginsFactory.getPlugin(item.plugin))
                .then((item: any) => this.items.push(item))
                .catch((errors: ResponseError[]) => {
                    errors.forEach(error => this.msgSrv.error(error.detail))
                });
        });
    }

    /**
     * Redirects to the view item page.
     * @param {PluginItem} item
     */
    view(item: PluginItem) {
        this.router
            .navigate(['plugins', item.plugin].concat(item.links.view), {
                relativeTo: this.route
            });
    }

    /**
     * Redirects to the edit item page.
     * @param {PluginItem} item
     */
    edit(item: PluginItem) {
        this.router
            .navigate(['plugins', item.plugin].concat(item.links.edit), {
                relativeTo: this.route
            });
    }

    /**
     * Deletes item from event.
     * @param {PluginItem} item
     */
    remove(item: PluginItem) {
        // First remove from server.
        this.itemSrv
            .delete(item.pluginId, PluginsFactory.getPlugin(item.plugin))
            .then(() => {
                // Then remove from local list.
                let index = this.items.indexOf(item);
                if (index !== -1) {
                    this.items.splice(index, 1);
                }
                this.msgSrv.success(`Item ${item.name} successfully removed.`);
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}

import {Component, Input} from '@angular/core';
import {OnInit} from '@angular/core';
import {Event} from "../../../events/models/event";
import {ItemService} from "../../services/item.service";
import {PluginsFactory} from "../../../plugins/plugins-factory";
import {PluginItem} from "../../../plugins/plugin-item";
import {Router, ActivatedRoute} from "@angular/router";


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
        private router: Router
    ) {}

    ngOnInit(): void {
        this.initPluginItems();
    }

    initPluginItems() {
        this.items = [];
        this.event.items.map(item => {
            this.itemSrv
                .get(item, PluginsFactory.getPlugin(item.plugin))
                .then((item: any) => this.items.push(item));
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
            .delete(item.appId)
            .then(response => {
                console.log(response);
                // Then remove from local list.
                let index = this.items.indexOf(item);
                if (index !== -1) {
                    console.log(item, 'removing from local list');
                    this.items.splice(index, 1);
                }
            })
            .catch(errors => console.log(errors));
    }



}

import {Component, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {PluginsFactory} from "./plugins-factory";


@Component({
    selector: 'plugins',
    templateUrl: 'plugins.component.html',
    styleUrls: [
        'plugins.component.css'
    ],
})

export class PluginsComponent implements OnInit {

    constructor(
        private route: ActivatedRoute,
    ) {}

    plugins: any[];

    private params: {
        eventId: string,
    };

    private sub: any;

    ngOnInit() {
        this.initParams();
        this.initPlugins();
    }

    private initPlugins() {
        this.plugins = PluginsFactory.listPlugins();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                eventId: params['id'],
            };
        });
    }

}

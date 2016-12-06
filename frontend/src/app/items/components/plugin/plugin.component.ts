import {Component} from '@angular/core';
import {ActivatedRoute} from "@angular/router";


@Component({
    selector: 'plugin',
    templateUrl: 'plugin.component.html',
})

export class PluginComponent {
    constructor(
        private route: ActivatedRoute
    ) {}

    plugin: string;
    private sub: any;

    ngOnInit() {
        this.initParams();
        this.initPluginComponent();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.plugin = params['plugin'];
        });
    }

    private initPluginComponent() {
        console.log(this.plugin, 'this.plugin')
    }

}

import {
    Component, ViewContainerRef, ComponentFactoryResolver, ViewChild, ComponentRef, OnInit,
    OnDestroy
} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {PluginsFactory} from "../../plugins-factory";


@Component({
    selector: 'plugin',
    templateUrl: 'plugin.component.html',
    entryComponents: PluginsFactory.listComponents()
})

export class PluginComponent implements OnInit, OnDestroy {
    constructor(
        private route: ActivatedRoute,
        private resolver: ComponentFactoryResolver
    ) {}

    private params: {
        eventId: string,
        plugin: string
    };

    private sub: any;

    // Component input
    @ViewChild('dynamicTarget', { read: ViewContainerRef })
    private dynamicTarget: any;

    // We'll need to keep track of our injected component to manage it correctly
    private componentReference: ComponentRef<Component>;

    ngOnInit() {
        this.initParams();
        this.initPluginComponent();
    }

    ngOnDestroy() {
        this.destroyComponent();
    }

    private destroyComponent() {
        if (this.componentReference) {
            this.componentReference.destroy();
        }
    }

    private initPluginComponent() {
        let plugin = PluginsFactory.getPlugin(this.params.plugin);
        if (plugin) {
            let componentFactory = this.resolver.resolveComponentFactory(plugin.component);
            this.componentReference = this.dynamicTarget.createComponent(componentFactory);
        }
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                eventId: params['id'],
                plugin: params['plugin']
            }
        });
    }

}

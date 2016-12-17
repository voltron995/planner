export abstract class PluginItem {
    appId: string;
    pluginId: string;
    plugin: string;
    name: string;
    image: string;
    links: {
        edit: Array<string>,
        view: Array<string>
    };

    constructor(appId: string, attributes: {
        pluginId: string;
        plugin: string;
        name: string;
        image: string;
    }) {
        this.appId = appId;
        this.pluginId = attributes.pluginId;
        this.plugin = attributes.plugin;
        this.name = attributes.name;
        this.image = attributes.image;
        this.links = this.initLinks();
    }

    protected abstract initLinks(): {
        edit: Array<string>,
        view: Array<string>
    };
}



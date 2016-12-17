export class Item {

    public id: string;
    public plugin: string;
    public pluginItemId: string;

    constructor(id: string, attributes: any) {
        this.id = id;
        this.plugin = attributes.plugin;
        this.pluginItemId = attributes.pluginItemId;
    }

    public static newFromResponse(data: any) {
        return new this(data.id, {
            plugin: data.plugin,
            pluginItemId: data.plugin_item_id
        });
    }

}

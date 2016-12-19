import {PluginItem} from "../plugin-item";

export class RecipesPluginItem extends PluginItem {
    protected initLinks() {
        return {
            edit: ['dishes', this.pluginId, 'edit'],
            view: ['dishes', this.pluginId],
        }
    }
}
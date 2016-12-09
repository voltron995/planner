import {RecipesPlugin} from "./recipes/recipes-plugin";
import {BasePlugin} from "./base-plugin";

export class PluginsFactory {

    static _plugins: BasePlugin[] = [
        new RecipesPlugin()
    ];

    public static getPlugin(slug: string) {
        return this._plugins.filter((plugin: BasePlugin) => plugin.slug == slug).pop();
    }

    public static listComponents() {
        return this._plugins.map((plugin: BasePlugin) => plugin.component);
    }

    public static listPlugins() {
        return this._plugins;
    }
}
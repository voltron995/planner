import {RecipesPlugin} from "./recipes/recipes-plugin";
import {BasePlugin} from "./base-plugin";
import {BooksPlugin, TravelsPlugin, MoviesPlugin, MusicPlugin, SportPlugin} from "./mock-plugins";

export class PluginsFactory {

    static _plugins: BasePlugin[] = [
        new RecipesPlugin(),
        new BooksPlugin(),
        new TravelsPlugin(),
        new MoviesPlugin(),
        new MusicPlugin(),
        new SportPlugin(),
    ];

    public static listPlugins() {
        // todo: remove concat
        return this._plugins.concat(this._plugins, this._plugins, this._plugins, this._plugins);
    }

    public static getPlugin(slug: string) {
        return this._plugins.filter((plugin: BasePlugin) => plugin.slug == slug).pop();
    }
}
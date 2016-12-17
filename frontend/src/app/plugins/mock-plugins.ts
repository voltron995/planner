import {BasePlugin} from "./base-plugin";
import {RecipesPluginItem} from "./recipes/recipes-plugin-item";

export class BooksPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Books';
    itemUrl = 'dishes';
    itemClass = RecipesPluginItem;
}

export class TravelsPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Travels';
    itemUrl = 'dishes';
    itemClass = RecipesPluginItem;
}

export class MoviesPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Movies';
    itemUrl = 'dishes';
    itemClass = RecipesPluginItem;
}

export class MusicPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Music';
    itemUrl = 'dishes';
    itemClass = RecipesPluginItem;
}

export class SportPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Sport';
    itemUrl = 'dishes';
    itemClass = RecipesPluginItem;
}
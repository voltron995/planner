import {BasePlugin} from "../base-plugin";
import {RecipesPluginItem} from "./recipes-plugin-item";

export class RecipesPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Recipes';
    itemUrl = 'dishes';
    itemClass = RecipesPluginItem
}
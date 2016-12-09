import {RecipesPluginComponent} from "./recipes-plugin.component";
import {BasePlugin} from "../base-plugin";

export class RecipesPlugin implements BasePlugin {
    slug = 'recipes';
    name = 'Recipes';
    component = RecipesPluginComponent
}
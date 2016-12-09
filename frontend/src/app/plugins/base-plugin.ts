import {Component} from "@angular/core";
import {Type} from "@angular/core/src/type";


export interface BasePlugin {
    slug: string;
    name: string;
    component: Type<Component>
}
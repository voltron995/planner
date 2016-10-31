import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {FormsModule} from "@angular/forms";

import {AppComponent} from './app.component';
import {EventDetailComponent} from './event-detail.component'

@NgModule({
    imports: [
        BrowserModule,
        FormsModule
    ],
    declarations: [
        AppComponent,
        EventDetailComponent
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {
}

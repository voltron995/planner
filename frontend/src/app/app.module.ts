import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';

import {AppRoutingModule} from './app-routing.module';

import {AppComponent} from './app.component';
import {EventDetailComponent} from './event-detail.component';
import {EventsComponent} from './events.component';
import {EventService} from './event.service';
import {ProfileEditComponent} from './profile-edit.component';


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AppRoutingModule
    ],
    declarations: [
        AppComponent,
        EventDetailComponent,
        EventsComponent,
        ProfileEditComponent
    ],
    providers: [
        EventService
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {
}

import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {FileSelectDirective} from 'ng2-file-upload'
import {ModalModule} from 'angular2-modal';
import {BootstrapModalModule} from 'angular2-modal/plugins/bootstrap';
import {ReactiveFormsModule} from '@angular/forms';

import {AppRoutingModule} from './app-routing.module';

import {AppComponent} from './app.component';
import {EventDetailComponent} from './events/components/event-detail.component';
import {EventsComponent} from './events/components/events.component';
import {EventService} from './events/services/event.service';
import {ProfileService} from './profiles/services/profile.service';
import {ProfileComponent} from './profiles/components/profile.component';
import {ProfileEditForm} from './profiles/forms/profile-edit.form';
import {RequestService} from './main/services/request.service';
import {ResponseService} from './main/services/response.service';
import {UserEditForm} from "./users/forms/user-edit.form";
import {UserService} from './users/services/user.service';


@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AppRoutingModule,
        ModalModule.forRoot(),
        BootstrapModalModule,
        ReactiveFormsModule
    ],
    declarations: [
        AppComponent,
        EventDetailComponent,
        EventsComponent,
        FileSelectDirective,
        ProfileComponent,
        ProfileEditForm,
        UserEditForm,
    ],
    providers: [
        EventService,
        ProfileService,
        UserService,
        RequestService,
        ResponseService
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {
}

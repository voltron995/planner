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
import {EventComponent} from './events/components/event.component';
import {EventsComponent} from './events/components/events.component';
import {EventService} from './events/services/event.service';
import {ProfileService} from './profiles/services/profile.service';
import {ProfileComponent} from './profiles/components/profile.component';
import {ProfileEditForm} from './profiles/forms/profile-edit.form';
import {RequestService} from './main/services/request.service';
import {ResponseService} from './main/services/response.service';
import {UserEditForm} from "./users/forms/user-edit.form";
import {UserService} from './users/services/user.service';
import {EventEditComponent} from "./events/components/event-edit.component";
import {EventEditForm} from "./events/forms/event-edit.form";


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
        EventComponent,
        EventEditComponent,
        EventsComponent,
        EventEditForm,
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

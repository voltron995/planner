import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';
import {FileUploadModule} from 'ng2-file-upload'
import {ModalModule} from 'angular2-modal';
import {BootstrapModalModule} from 'angular2-modal/plugins/bootstrap';
import {ReactiveFormsModule} from '@angular/forms';

import {AppRoutingModule} from './main/modules/app-routing.module';

import {AppComponent} from './main/components/app/app.component';
import {EventComponent} from './events/components/event/event.component';
import {EventsComponent} from './events/components/events/events.component';
import {EventService} from './events/services/event.service';
import {ProfileService} from './profiles/services/profile.service';
import {ProfileComponent} from './profiles/components/profile/profile.component';
import {ProfileEditForm} from './profiles/forms/profile-edit/profile-edit.form';
import {RequestService} from './main/services/request.service';
import {ResponseService} from './main/services/response.service';
import {UserEditForm} from "./users/forms/user-edit/user-edit.form";
import {UserService} from './users/services/user.service';
import {EventEditComponent} from "./events/components/event-edit/event-edit.component";
import {EventEditForm} from "./events/forms/event-edit/event-edit.form";
import {EventCreateComponent} from "./events/components/event-create/event-create.component";
import {EventCreateForm} from "./events/forms/event-create/event-create.form";
import {PluginsComponent} from "./plugins/plugins.component";
import {MasonryModule} from "angular2-masonry/src/module";
import { CalendarModule } from 'angular-calendar';
import {CalendarComponent} from "./events/components/calendar/calendar.component";
import {Ng2DatetimePickerModule} from "ng2-datetime-picker";
import {EventDeleteComponent} from "./events/components/event-delete/event-delete.component";
import {TargetsComponent} from './targets/components/target-list/target-list.component';
import {TargetComponent} from "./targets/components/target-single/target-single.component";
import {TargetEditComponent} from "./targets/components/target-edit/target-edit.component";
import {TargetDeleteComponent} from "./targets/components/target-delete/target-delete.component";
import {TargetCreateComponent} from "./targets/components/target-create/target-create.component";
import {TargetService} from './targets/services/target.service';
import {TargetEditForm} from "./targets/forms/target-edit/target-edit.form";
import {TargetCreateForm} from "./targets/forms/target-create/target-create.form";
import {ItemsComponent} from "./items/components/items/items.component";
import {ItemService} from "./items/services/item.service";




@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        HttpModule,
        AppRoutingModule,
        ModalModule.forRoot(),
        BootstrapModalModule,
        ReactiveFormsModule,
        MasonryModule,
        CalendarModule.forRoot(),
        Ng2DatetimePickerModule,
        FileUploadModule,
    ],
    declarations: [
        AppComponent,
        EventComponent,
        EventCreateComponent,
        EventEditComponent,
        EventDeleteComponent,
        EventsComponent,
        EventCreateForm,
        EventEditForm,
        ItemsComponent,
        TargetComponent,
        TargetCreateComponent,
        TargetEditComponent,
        TargetsComponent,
        TargetCreateForm,
        TargetDeleteComponent,
        TargetEditForm,
        PluginsComponent,
        ProfileComponent,
        ProfileEditForm,
        UserEditForm,
        CalendarComponent,
    ],
    providers: [
        EventService,
        ItemService,
        ProfileService,
        UserService,
        TargetService,
        RequestService,
        ResponseService
    ],
    bootstrap: [
        AppComponent
    ]
})

export class AppModule {
}

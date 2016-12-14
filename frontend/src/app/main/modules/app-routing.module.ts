import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventsComponent} from '../../events/components/events/events.component';
import {ProfileComponent} from '../../profiles/components/profile/profile.component';
import {EventComponent} from "../../events/components/event/event.component";
import {EventEditComponent} from "../../events/components/event-edit/event-edit.component";
import {EventCreateComponent} from "../../events/components/event-create/event-create.component";
import {TargetsComponent} from '../../targets/components/target-list/target-list.component';
import {TargetComponent} from "../../targets/components/target-single/target-single.component";
import {TargetEditComponent} from "../../targets/components/target-edit/target-edit.component";
import {TargetCreateComponent} from "../../targets/components/target-create/target-create.component";
import {TargetDeleteComponent} from "../../targets/components/target-delete/target-delete.component";

const routes: Routes = [
  {
    path: 'events',
    component: EventsComponent
  },
  {
    path: 'events/new',
    component: EventCreateComponent
  },
  {
    path: 'events/:id',
    component: EventComponent
  },
  {
    path: 'events/:id/edit',
    component: EventEditComponent
  },
  {
    path: 'profile',
    component: ProfileComponent
  },
  {
    path: 'targets',
    component: TargetsComponent
  },
  {
    path: 'targets/new',
    component: TargetCreateComponent
  },
  {
    path: 'targets/:id',
    component: TargetComponent
  },
  {
    path: 'targets/:id/edit',
    component: TargetEditComponent
  },
  {
    path: 'targets/:id/delete',
    component: TargetDeleteComponent
  },
];

@NgModule({
    imports: [
        RouterModule.forRoot(routes)
    ],
    exports: [
        RouterModule
    ]
})

export class AppRoutingModule {
}

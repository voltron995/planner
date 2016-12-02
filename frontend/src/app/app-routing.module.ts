import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventsComponent} from './events/components/events.component';
import {ProfileComponent} from './profiles/components/profile.component';
import {EventComponent} from "./events/components/event.component";
import {EventEditComponent} from "./events/components/event-edit.component";
import {EventCreateComponent} from "./events/components/event-create.component";

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
  }
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

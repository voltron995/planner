import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventsComponent} from '../../events/components/events/events.component';
import {ProfileComponent} from '../../profiles/components/profile/profile.component';
import {EventComponent} from "../../events/components/event/event.component";
import {EventEditComponent} from "../../events/components/event-edit/event-edit.component";
import {EventCreateComponent} from "../../events/components/event-create/event-create.component";
import {ItemCreateComponent} from "../../items/components/item-create/item-create.component";

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
    path: 'events/:id/item/new',
    component: ItemCreateComponent
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

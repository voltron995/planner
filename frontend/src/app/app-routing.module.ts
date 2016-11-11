import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventsComponent} from './events.component';
import {ProfileEditComponent} from './profile-edit.component';

const routes: Routes = [
  {
    path: 'events',
    component: EventsComponent
  },
  {
    path: 'profile',
    component: ProfileEditComponent
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

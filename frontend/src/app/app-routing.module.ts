import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventsComponent} from './events/components/events.component';
import {ProfileComponent} from './profiles/components/profile.component';

const routes: Routes = [
  {
    path: 'events',
    component: EventsComponent
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

import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventsComponent} from '../../events/components/events/events.component';
import {ProfileComponent} from '../../profiles/components/profile/profile.component';
import {EventComponent} from "../../events/components/event/event.component";
import {EventEditComponent} from "../../events/components/event-edit/event-edit.component";
import {EventCreateComponent} from "../../events/components/event-create/event-create.component";
import {PluginsComponent} from "../../plugins/plugins.component";
import {TargetsComponent} from '../../targets/components/target-list/target-list.component';
import {TargetComponent} from "../../targets/components/target-single/target-single.component";
import {TargetEditComponent} from "../../targets/components/target-edit/target-edit.component";
import {TargetCreateComponent} from "../../targets/components/target-create/target-create.component";
import {RecipesPluginModule} from "../../plugins/recipes/recipes-plugin.module";
import {NotFoundComponent} from "../../errors/components/not-found/not-found.component";

const routes: Routes = [
    {
      path: '',
      redirectTo: '/events',
      pathMatch: 'full'
    },
    {
        path: 'events',
        children: [
            {
                path: '',
                component: EventsComponent,
            },
            {
                path: 'new',
                component: EventCreateComponent
            },
            {
                path: ':id',
                children: [
                    {
                        path: '',
                        component: EventComponent,
                    },
                    {
                        path: 'edit',
                        component: EventEditComponent
                    },
                    {
                        path: 'plugins',
                        children: [
                            {
                                path: '',
                                component: PluginsComponent,
                            },
                            {
                                path: 'recipes',
                                loadChildren: () => RecipesPluginModule,
                            }
                        ]
                    },
                ]
            },
        ]
    },
    {
        path: 'profile',
        component: ProfileComponent
    },
    {
        path: 'targets',
        children: [
            {
                path: '',
                component: TargetsComponent
            },
            {
                path: 'new',
                component: TargetCreateComponent
            },
            {
                path: ':id',
                children: [
                    {
                        path: '',
                        component: TargetComponent
                    },
                    {
                        path: 'edit',
                        component: TargetEditComponent
                    },
                ]
            },
        ]
    },
    {
        path: '**',
        component: NotFoundComponent
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

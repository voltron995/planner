import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {Event} from '../../models/event'
import {EventService} from "../../services/event.service";
import {Location} from '@angular/common';


@Component({
    selector: 'event-delete',
    templateUrl: 'event-delete.component.html',
    styleUrls: [
        'event-delete.component.css'
    ],

})

export class EventDeleteComponent implements OnInit, OnDestroy {
    constructor(
        private route: ActivatedRoute,
        private eventSrv: EventService,
        private router : Router
    ) {}

    id: string;
    event: Event;
    private sub:any;

    ngOnInit() {
        this.initParams();
        this.initEvent();

    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.id = params['id'];
        });
    }

    private initEvent() {
        this.eventSrv
            .delete(this.id)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
      this.router.navigate(['/events']);
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

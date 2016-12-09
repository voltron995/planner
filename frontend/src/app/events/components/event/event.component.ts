import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Event} from '../../models/event'
import {EventService} from "../../services/event.service";


@Component({
    selector: 'event',
    templateUrl: 'event.component.html',
    styleUrls: [
        'event.component.css'
    ],

})

export class EventComponent implements OnInit, OnDestroy {
    constructor(
        private route: ActivatedRoute,
        private eventSrv: EventService
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
            .get(this.id)
            .then(event => {
                this.event = event;
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}
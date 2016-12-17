import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Event} from '../../models/event'
import {EventService} from "../../services/event.service";
import {Subscription} from "rxjs";
import {Target} from "../../../targets/models/targets";
import {TargetService} from "../../../targets/services/target.service";


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
        private eventSrv: EventService,
        private targetSrv: TargetService,
    ) {}

    event: Event;

    target: Target;

    params: {
        id: string,
    };

    private sub: Subscription;

    ngOnInit() {
        this.initParams();
        this.initEvent();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                id: params['id']
            };
        });
    }

    private initEvent() {
        this.eventSrv
            .get(this.params.id)
            .then(event => {
                this.event = event;
                this.initTarget();
            });
    }

    private initTarget() {
        this.targetSrv
            .get(this.event.target_id)
            .then(target => this.target = target);
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

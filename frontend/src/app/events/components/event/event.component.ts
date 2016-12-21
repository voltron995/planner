import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {Event} from '../../models/event'
import {EventService} from "../../services/event.service";
import {Subscription} from "rxjs";
import {Target} from "../../../targets/models/targets";
import {TargetService} from "../../../targets/services/target.service";
import {MessageService} from "../../../main/services/message.service";
import {ResponseError} from "../../../main/models/errors";


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
        private router: Router,
        private msgSrv: MessageService
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

    deleteEvent() {
        this.eventSrv
            .delete(this.event.id)
            .then(event => {
                this.msgSrv.success(`Event ${this.event.name} successfully deleted.`);
                this.router.navigate(['/events']);
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });

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
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });

    }

    private initTarget() {
        this.targetSrv
            .get(this.event.targetId)
            .then(target => this.target = target)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

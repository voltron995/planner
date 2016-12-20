import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Event} from '../../models/event'
import {EventService} from "../../services/event.service";
import {Target} from '../../../targets/models/targets';
import {TargetService} from '../../../targets/services/target.service';
import {Subscription} from "rxjs";
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";

@Component({
    selector: 'event-edit',
    templateUrl: 'event-edit.component.html',
    styleUrls: [
        'event-edit.component.css'
    ],

})

export class EventEditComponent implements OnInit, OnDestroy {
    targets: Target[];

    constructor(
        private route: ActivatedRoute,
        private eventSrv: EventService,
        private targetSrv: TargetService,
        private msgSrv: MessageService,
    ) {}

    params: {
        id: string
    };

    event: Event;

    private sub: Subscription;

    ngOnInit() {
        this.initParams();
        this.initEvent();
        this.initTargets();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                id: params['id']
            }
        });
    }

    private initEvent() {
        this.eventSrv
            .get(this.params.id)
            .then(event => this.event = event)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    initTargets(): void {
        this.targetSrv
            .list()
            .then(targets => this.targets = targets)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

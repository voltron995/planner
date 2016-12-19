import {Component} from '@angular/core';
import {OnInit} from '@angular/core';

import {Event} from '../../models/event';
import {EventService} from '../../services/event.service';
import {Target} from '../../../targets/models/targets';
import {TargetService} from '../../../targets/services/target.service';
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";
import {isUndefined} from "util";


@Component({
    selector: 'events',
    templateUrl: 'events.component.html',
    styleUrls: [
        'events.component.css'
    ]
})

export class EventsComponent implements OnInit {

    events: Event[];

    targets: Target[];

    constructor(
        private eventSrv: EventService,
        private targetSrv: TargetService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.getEvents();
        this.getTargets();
    }

    getEvents(): void {
        this.eventSrv
            .list()
            .then(events => this.events = events)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    getTargets(): void {
        this.targetSrv
            .list()
            .then(targets => this.targets = targets)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    isCalendarReady() {
        return !isUndefined(this.events)
    }

}

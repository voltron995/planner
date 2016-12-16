import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Event} from '../../models/event'
import {EventService} from "../../services/event.service";
import {Target} from '../../../targets/models/targets';
import {TargetService} from '../../../targets/services/target.service';

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
        private targetService: TargetService
    ) {}

    id: string;
    event: Event;
    private sub:any;

    ngOnInit() {
        this.initParams();
        this.initEvent();
        this.getTargets();
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

    getTargets(): void {
        this.targetService
            .list()
            .then(targets => this.targets = targets);
    }


    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

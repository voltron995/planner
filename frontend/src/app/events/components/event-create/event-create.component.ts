import {Component, OnInit} from '@angular/core';
import {Target} from '../../../targets/models/targets';
import {TargetService} from '../../../targets/services/target.service';
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";

@Component({
    selector: 'event-create',
    templateUrl: 'event-create.component.html',
    styleUrls: [
        'event-create.component.css'
    ],

})

export class EventCreateComponent implements OnInit {

	targets: Target[];

    constructor(
        private targetSrv: TargetService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initTargets();
    }

    initTargets(): void {
        this.targetSrv
            .list()
            .then(targets => this.targets = targets)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }
}

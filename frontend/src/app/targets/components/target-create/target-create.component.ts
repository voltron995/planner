import {Component, OnInit} from '@angular/core';
import {Target} from "../../models/targets";
import {TargetService} from "../../services/target.service";
import {MessageService} from "../../../main/services/message.service";
import {ResponseError} from "../../../main/models/errors";


@Component({
    selector: 'target-create',
    templateUrl: 'target-create.component.html',
    styleUrls: [
        'target-create.component.css'
    ],

})

export class TargetCreateComponent implements OnInit {

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

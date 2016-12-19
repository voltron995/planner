import {Component, OnInit} from '@angular/core';
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";


@Component({
    selector: 'target-list',
    templateUrl: 'target-list.component.html',
    styleUrls: [
        'target-list.component.css'
    ],
    providers: [
        TargetService
    ]
})

export class TargetsComponent implements OnInit {

    targets: Target[];

    selectedTarget: Target;

    constructor(
        private targetSrv: TargetService,
        private msgSrv: MessageService
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

    onSelect(target: Target): void {
        this.selectedTarget = target;
    }
}
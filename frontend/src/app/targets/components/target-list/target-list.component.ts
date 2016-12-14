import {Component, OnInit, OnDestroy} from '@angular/core';
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";


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

    constructor(private targetService: TargetService) {
    }

    ngOnInit(): void {
        this.getTargets();
    }

    getTargets(): void {
        this.targetService
            .list()
            .then(targets => this.targets = targets);
    }

    onSelect(target: Target): void {
        this.selectedTarget = target;
    }
}
import {Component, OnInit} from '@angular/core';
import {Target} from '../../../targets/models/targets';
import {TargetService} from '../../../targets/services/target.service';

@Component({
    selector: 'event-create',
    templateUrl: 'event-create.component.html',
    styleUrls: [
        'event-create.component.css'
    ],

})

export class EventCreateComponent implements OnInit {
	targets: Target[];

    constructor(private targetService: TargetService) {}

    ngOnInit(): void {
        this.getTargets();
    }

    getTargets(): void {
        this.targetService
            .list()
            .then(targets => this.targets = targets);
    }
}

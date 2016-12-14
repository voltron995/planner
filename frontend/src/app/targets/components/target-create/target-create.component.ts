import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";


@Component({
    selector: 'target-create',
    templateUrl: 'target-create.component.html',
    styleUrls: [
        'target-create.component.css'
    ],

})

export class TargetCreateComponent implements OnInit, OnDestroy {
    constructor(
        private route: ActivatedRoute,
        private targetSrv: TargetService
    ) {}

    name: string;
    description: string;
    target: Target;
    private sub:any;

    ngOnInit() {
        this.initParams();
        this.initTarget();

    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.name = params['name'];
            this.description = params['description'];
        });
    }

    private initTarget() {
        this.targetSrv
            .post(this.target)  // ???
            .then(target => {
                this.target = target;
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

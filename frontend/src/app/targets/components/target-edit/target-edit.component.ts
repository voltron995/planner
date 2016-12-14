import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";


@Component({
    selector: 'target-edit',
    templateUrl: 'target-edit.component.html',
    styleUrls: [
        'target-edit.component.css'
    ],

})

export class TargetEditComponent implements OnInit, OnDestroy {
    constructor(
        private route: ActivatedRoute,
        private targetSrv: TargetService
    ) {}

    id: string;
    target: Target;
    private sub:any;

    ngOnInit() {
        this.initParams();
        this.initTarget();

    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.id = params['id'];
        });
    }

    private initTarget() {
        this.targetSrv
            .get(this.id)
            .then(target => {
                this.target = target;
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

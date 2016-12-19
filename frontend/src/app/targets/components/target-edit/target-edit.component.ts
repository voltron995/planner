import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";
import {Subscription} from "rxjs";


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

    params: {
        id: string
    };

    target: Target;

    private sub: Subscription;

    ngOnInit() {
        this.initParams();
        this.initTarget();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                id: params['id']
            }
        });
    }

    private initTarget() {
        this.targetSrv
            .get(this.params.id)
            .then(target => {
                this.target = target;
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

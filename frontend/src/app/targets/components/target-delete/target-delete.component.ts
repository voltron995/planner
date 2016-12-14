import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";


@Component({
    selector: 'target-delete',
    templateUrl: 'target-delete.component.html',
    styleUrls: [
        'target-delete.component.css'
    ],

})

export class TargetDeleteComponent implements OnInit, OnDestroy {
    constructor(
        private route: ActivatedRoute,
        private targetSrv: TargetService
    ) {}

    id: string;
    target: Target;
    private sub:any;

    ngOnInit() {
        this.initParams();
        this.deleteTarget();

    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.id = params['id'];
        });
    }

    private deleteTarget(): void {
        this.targetSrv
            .delete(this.id)
            .then(this.target = null
            );

    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";
import {Subscription} from "rxjs";
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";


@Component({
    selector: 'target-edit',
    templateUrl: 'target-edit.component.html',
    styleUrls: [
        'target-edit.component.css'
    ],

})

export class TargetEditComponent implements OnInit, OnDestroy {
    targets: Target[];

    constructor(
        private route: ActivatedRoute,
        private targetSrv: TargetService,
        private msgSrv: MessageService
    ) {}

    params: {
        id: string
    };

    target: Target;

    private sub: Subscription;

    ngOnInit() {
        this.initParams();
        this.initTarget();
        this.initTargets();
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

    initTargets(): void {
        this.targetSrv
            .list()
            .then(targets => this.targets = targets)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }
}

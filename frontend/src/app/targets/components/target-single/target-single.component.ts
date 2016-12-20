import {Component, OnInit, OnDestroy} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {Target} from '../../models/targets'
import {TargetService} from "../../services/target.service";
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";
import {Subscription} from "rxjs";


@Component({
    selector: 'target',
    templateUrl: 'target-single.component.html',
    styleUrls: [
        'target-single.component.css'
    ],
})

export class TargetComponent implements OnInit, OnDestroy {

    constructor(
        private route: ActivatedRoute,
        private targetSrv: TargetService,
        private router: Router,
        private msgSrv: MessageService
    ) {}

    params: {
        id: string,
    };

    target: Target;

    private sub: Subscription;

    ngOnInit() {
        this.initParams();
        this.initTarget();
    }

    deleteTarget(): void {
        this.targetSrv
            .delete(this.target.id)
            .then(() => {
                this.msgSrv.success(`Target ${this.target.name} successfully deleted.`);
                this.router.navigate(['/events']);
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                id: params['id']
            };
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

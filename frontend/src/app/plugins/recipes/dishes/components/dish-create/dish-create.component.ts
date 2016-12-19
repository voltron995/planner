import {Component, OnInit} from '@angular/core';
import {Subscription} from "rxjs";
import {ActivatedRoute} from "@angular/router";


@Component({
    selector: 'dish-create',
    templateUrl: 'dish-create.component.html',
    styleUrls: [
        'dish-create.component.css'
    ],
})

export class DishCreateComponent implements OnInit {

    private params: {
        eventId: string,
    };

    private sub: Subscription;

    constructor(
        private route: ActivatedRoute
    ) {}

    ngOnInit() {
        this.initParams();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                eventId: params['id'],
            };
        });
    }


}

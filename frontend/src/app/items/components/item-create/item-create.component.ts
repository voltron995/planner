import {Component} from '@angular/core';
import {ActivatedRoute} from "@angular/router";


@Component({
    selector: 'item-create',
    templateUrl: 'item-create.component.html',
    styleUrls: [
        'item-create.component.css'
    ],

})

export class ItemCreateComponent {
    constructor(
        private route: ActivatedRoute
    ) {}

    event_id: string;
    private sub: any;

    ngOnInit() {
        this.initParams();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.event_id = params['id'];
        });
    }

}

import {Component, OnInit} from '@angular/core';
import {Subscription} from "rxjs";
import {ActivatedRoute} from "@angular/router";
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";
import {ResponseError} from "../../../../../main/models/errors";
import {MessageService} from "../../../../../main/services/message.service";


@Component({
    selector: 'dish-edit',
    templateUrl: 'dish-edit.component.html',
    styleUrls: [
        'dish-edit.component.css'
    ],
})

export class DishEditComponent implements OnInit {

    dish: Dish;

    private params: {
        eventId: string,
        dishId: string,
    };

    private sub: Subscription;

    constructor(
        private route: ActivatedRoute,
        private dishSrv: DishService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit() {
        this.initParams();
        this.initDish();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            this.params = {
                eventId: params['id'],
                dishId: params['dish_id'],
            };
        });
    }

    private initDish() {
        this.dishSrv
            .get(this.params.dishId)
            .then((dish: Dish) => this.dish = dish)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}

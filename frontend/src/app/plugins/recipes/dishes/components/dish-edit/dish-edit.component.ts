import {Component, OnInit} from '@angular/core';
import {Subscription} from "rxjs";
import {ActivatedRoute} from "@angular/router";
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";


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
        private dishSrv: DishService
    ) {}

    ngOnInit() {
        this.initParams();
        this.initDish();
    }

    private initParams() {
        this.sub = this.route.params.subscribe(params => {
            console.log(params, 'params');
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
            .catch(errors => console.log(errors));
    }


}

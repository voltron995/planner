import {Component, OnInit, OnDestroy} from '@angular/core';
import {DishService} from "../../../dishes/services/dish.service";
import {Dish} from "../../models/dish";
import {ActivatedRoute} from "@angular/router";
import {Subscription} from "rxjs";

@Component({
    selector: 'dish',
    templateUrl: 'dish.component.html',
    styleUrls: [
        'dish.component.css'
    ]
})
export class DishComponent implements OnInit, OnDestroy {

    dish: Dish;

    private params: {
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
            this.params = {
                dishId: params['dish_id'],
            };
        });
    }

    private initDish() {
        this.dishSrv
            .get(this.params.dishId)
            .then(dish => (this.dish = dish));
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }

}
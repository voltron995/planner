import {Component, OnInit, OnDestroy} from '@angular/core';
import {DishService} from "../../../dishes/services/dish.service";
import {Dish} from "../../models/dish";
import {ActivatedRoute, Router} from "@angular/router";
import {Subscription} from "rxjs";
import {ResponseError} from "../../../../../main/models/errors";
import {MessageService} from "../../../../../main/services/message.service";

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
        eventId: string,
        dishId: string,
    };

    private sub: Subscription;

    constructor(
        private route: ActivatedRoute,
        private dishSrv: DishService,
        private msgSrv: MessageService,
        private router: Router,
    ) {}

    ngOnInit() {
        this.initParams();
        this.initDish();
    }

    deleteDish() {
        this.dishSrv
            .delete(this.dish.id)
            .then(() => {
                this.msgSrv.success(`Dish ${this.dish.name} successfully deleted.`);
                this.router.navigate(['/events', this.params.eventId]);
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
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
            .then(dish => (this.dish = dish))
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }

}

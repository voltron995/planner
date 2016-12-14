import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {Router} from '@angular/router'
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";

@Component({
    selector: 'dish-create-form',
    templateUrl: 'dish-create.form.html',
    styleUrls: [
        'dish-create.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class DishCreateForm implements OnInit {

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private dishSrv: DishService,
        private router: Router
    ) {

    }

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          name: [''],
          description: [''],
        });
    }

    onSubmit() {
        let values = this.form.value;
        console.log(values);
        this.dishSrv
            .post(values)
            .then((dish: Dish) => console.log(dish, 'success'))
            .catch(errors => console.log(errors, 'errors'));
        // this.router.navigate(['/events'])
    }

}
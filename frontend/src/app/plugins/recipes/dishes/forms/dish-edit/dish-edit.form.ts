import {Component, Input, Output, OnInit, AfterContentInit} from '@angular/core';
import {FormBuilder, FormGroup, FormArray, FormControl} from '@angular/forms';
import {SelectModule} from 'angular2-select';
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";
import {FileUploader} from "ng2-file-upload";
import {Router} from "@angular/router";
import {MessageService} from "../../../../../main/services/message.service";
import {ResponseError} from "../../../../../main/models/errors";
import {Ingredient} from "../../../ingredients/models/ingredients";
import {IngredientService} from "../../../ingredients/services/ingredients.service";
import {DishIngredient} from "../../../ingredients/models/dish-ingredient";

@Component({
    selector: 'dish-edit-form',
    templateUrl: 'dish-edit.form.html',
    styleUrls: [
        'dish-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class DishEditForm {

    @Input()
    eventId: string;

    @Input()
    dish: Dish;

    uploader: FileUploader;
    imagePreview: string;

    ingredients: {
        list: Ingredient[],
        selected: DishIngredient[],
        options: Array<{
            label: string,
            value: string,
        }>,
    };

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private ingredientService: IngredientService,
        private dishSrv: DishService,
        private router: Router,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initForm();
        this.initIngredientList();
        this.initUploader();
    };

    initIngredientList(): void {
        this.ingredients = {
            list: [],
            options: [],
            selected: [],
        };

        this.ingredientService
            .list()
            .then(ingredients => {
                this.ingredients.list = ingredients;
                this.initSelectedIngredients();
                this.initIngredientOptions();
                this.initIngredientsFormArray();
            });
    }

    initIngredientOptions() {
        let options: Array<{
            label: string,
            value: string,
        }> = [];

        this.ingredients.list
            .forEach((ingredient: Ingredient) => {
                let selected = this.ingredients.selected
                    .filter((selected: DishIngredient) => {
                        return selected.ingredient.id == ingredient.id;
                    }).pop();

                if (!selected) {
                    options.push({
                        value: ingredient.id.toString(),
                        label: ingredient.name.toString()
                    });
                }
            });

        this.ingredients.options = options;
    };

    initSelectedIngredients() {
        this.ingredients.selected = this.dish.ingredients;
    }

    protected initForm() {
        this.form = this.fb.group({
            name: [this.dish.name],
            description: [this.dish.description],
            image: [this.dish.image || ''],
            ingredients: this.fb.array([]),
            event_id: this.eventId
        });
    }

    protected initIngredientsFormArray(): void {
        let control = <FormArray>this.form.controls['ingredients'];
        this.ingredients.selected
            .forEach((ingredient: DishIngredient) => {
                control.push(this.fb.group({
                    id: ingredient.ingredient.id,
                    quantity: ingredient.quantity
                }));
            }, this);
    }

    onRemoveIngredient(index: number) {
        let control = <FormArray>this.form.controls['ingredients'];
        control.removeAt(index);
        this.ingredients.selected.splice(index, 1);
        this.initIngredientOptions();
    }

    onIngredientSelected(item: any): void {
        let selected = this.ingredients.list
            .filter((ingredient: Ingredient) => {
                return ingredient.id == item.value;
            }).pop();

        let duplicated = this.ingredients.selected
            .filter((ingredient: DishIngredient) => {
                return ingredient.ingredient.id == selected.id;
            }).pop();

        if (duplicated) {
            this.msgSrv.error('Ingredient already selected.');
        } else {
            this.ingredients.selected.push(new DishIngredient(0, selected));
            let control = <FormArray>this.form.controls['ingredients'];
            control.push(this.fb.group({
                id: selected.id,
                quantity: 0
            }));
            this.initIngredientOptions();
        }
    }

    initUploader() {
        let __this = this;
        let uploader = new FileUploader({
            url: '/api/v1.0/uploads/dish-images',
            autoUpload: true,
            removeAfterUpload: true
        });

        uploader.onCompleteItem = function (item: any, response: string, status: number) {
            var json = JSON.parse(response);
            __this.imagePreview = json.link;
            __this.form.patchValue({'image': json.id});
        };

        this.uploader = uploader;
        this.imagePreview = this.dish.imageLink;
    }


    onSubmit() {
        let values = this.form.value;
        values.ingredients = values.ingredients.map((value: any) => {
            return {
                'quantity': value.quantity,
                'ingredient': {
                    id: value.id,
                }
            }
        });

        this.dishSrv
            .put(this.dish.id, values)
            .then((dish: Dish) => {
                this.msgSrv.success(`Dish ${dish.name} successfully updated.`);
                this.router.navigate(['events', this.eventId, 'plugins', 'recipes', 'dishes', dish.id])
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }
}

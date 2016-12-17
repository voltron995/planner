import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";
import {FileUploader} from "ng2-file-upload";
import {Router} from "@angular/router";

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

export class DishEditForm implements OnInit {

    @Input()
    eventId: string;

    @Input()
    dish: Dish;

    uploader: FileUploader;
    imagePreview: string;

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private dishSrv: DishService,
        private router: Router
    ) {}

    ngOnInit(): void {
        this.initForm();
        this.initUploader();
    }

    initForm() {
        this.form = this.fb.group({
            name: [this.dish.name],
            description: [this.dish.description],
            img_path: [this.dish.image],
            ingredients: [[]],
            event_id: this.eventId,
        });
    }

    initUploader() {
        let _this = this;
        let uploader = new FileUploader({
            url: '/api/v1.0/uploads/dish-images',
            autoUpload: true,
            removeAfterUpload: true
        });

        uploader.onCompleteItem = function (item: any, response: string, status: number) {
            var json = JSON.parse(response);
            _this.imagePreview = json.link;
            _this.form.patchValue({'img_path': json.id});
        };

        _this.uploader = uploader;
        _this.imagePreview = this.dish.imageLink;
    }

    onSubmit() {
        let values = this.form.value;
        this.dishSrv
            .put(this.dish.id, values)
            .then((dish: Dish) => this.router.navigate(['events', this.eventId]))
            .catch(errors => console.log(errors, 'errors'));
    }

}
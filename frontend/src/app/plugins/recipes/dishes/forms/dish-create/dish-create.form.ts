import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {DishService} from "../../services/dish.service";
import {Dish} from "../../models/dish";
import {FileUploader} from "ng2-file-upload";
import {Router} from "@angular/router";

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

    @Input()
    eventId: string;
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
            name: [],
            description: [],
            img_path: [],
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
        _this.imagePreview = '/dist/assets/dish-default.jpg';
    }

    onSubmit() {
        let values = this.form.value;
        this.dishSrv
            .post(values)
            .then((dish: Dish) => this.router.navigate(['events', this.eventId, 'plugins', 'recipes']))
            .catch(errors => console.log(errors, 'errors'));
    }

}
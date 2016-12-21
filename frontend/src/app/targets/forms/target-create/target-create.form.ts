import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {TargetService} from '../../services/target.service';
import {Router} from '@angular/router';
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";
import {Target} from "../../models/targets";

@Component({
    selector: 'target-create-form',
    templateUrl: 'target-create.form.html',
    styleUrls: [
        'target-create.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class TargetCreateForm implements OnInit {

    @Input()
    targets: Target[];

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private targetService: TargetService,
        private router: Router,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
            name: [''],
            target_id: [null],
            description: [''],
        });
    }

    onSubmit() {
        let values = this.form.value;
        if (!values.target_id) {
            delete values.target_id;
        }
        this.targetService
            .post(values)
            .then(target => {
                this.msgSrv.success(`Target ${target.name} successfully created.`);
                this.router.navigate(['/events'])
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}
import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {TargetService} from '../../services/target.service';
import {Target} from '../../models/targets';
import {MessageService} from "../../../main/services/message.service";
import {ResponseError} from "../../../main/models/errors";
import {Router} from "@angular/router";

@Component({
    selector: 'target-edit-form',
    templateUrl: 'target-edit.form.html',
    styleUrls: [
        'target-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class TargetEditForm implements OnInit {

    @Input()
    target: Target;

    @Input()
    targets: Target[];

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private targetService: TargetService,
        private msgSrv: MessageService,
        private router: Router
    ) {}

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
            name: [this.target.name],
            target_id: [this.target.target_id],
            description: [this.target.description],
            is_done: [this.target.is_done],
        });

    }

    onSubmit() {
        let values = this.form.value;
        if (!values.target_id) {
            delete values.target_id;
        }
        this.targetService
            .put(this.target.id, values)
            .then(target => {
                this.msgSrv.success(`Target ${target.name} successfully saved.`);
                this.router.navigate(['/events'])
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}
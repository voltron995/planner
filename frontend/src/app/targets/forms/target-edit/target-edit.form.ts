import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {TargetService} from '../../services/target.service';
import {Target} from '../../models/targets';

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

    @Input() target: Target;
    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private targetService: TargetService
    ) {

    }

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          name: [this.target.name],
          description: [this.target.description],
          is_done: [this.target.is_done],
        });
    }

    onSubmit() {
        let values = this.form.value;
        this.targetService
            .put(this.target.id, values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
    }

}
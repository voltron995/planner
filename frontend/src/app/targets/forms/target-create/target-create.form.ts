import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {TargetService} from '../../services/target.service';
import { Router} from '@angular/router';

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

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private targetService: TargetService,
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
        this.targetService
            .post(values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
            this.router.navigate(['/events']);
    }

}
import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {User} from '../../users/models/user';
import {UserService} from '../services/user.service';

@Component({
    selector: 'user-edit-form',
    templateUrl: './user-edit.form.html',
    styleUrls: [
        './user-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class UserEditForm implements OnInit {

    @Input() user: User;
    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private userService: UserService
    ) {

    }

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          password: [''],
          confirm: [''],
        });
    }

    onSubmit() {
        console.log('submit');
        let values = this.form.value;
        this.form.reset();
        this.userService
            .putCurrent(values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
    }

}
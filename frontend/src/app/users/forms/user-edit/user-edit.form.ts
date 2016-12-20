import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {User} from '../../models/user';
import {UserService} from '../../services/user.service';
import {MessageService} from "../../../main/services/message.service";
import {ResponseError} from "../../../main/models/errors";

@Component({
    selector: 'user-edit-form',
    templateUrl: 'user-edit.form.html',
    styleUrls: [
        'user-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class UserEditForm implements OnInit {

    @Input()
    user: User;

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private userSrv: UserService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          old_password:[''],
          password: [''],
          confirm: [''],
        });
    }

    onSubmit() {
        let values = this.form.value;
        this.form.reset();
        this.userSrv
            .putCurrent(values)
            .then(() => this.msgSrv.success('Settings successfully saved.'))
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}

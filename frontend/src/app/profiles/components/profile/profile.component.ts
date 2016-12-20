import {Component, OnInit} from '@angular/core';
import {User} from '../../../users/models/user';
import {UserService} from '../../../users/services/user.service';
import {ResponseError} from "../../../main/models/errors";
import {MessageService} from "../../../main/services/message.service";

@Component({
    selector: 'profile',
    templateUrl: 'profile.component.html',
    styleUrls: [
        'profile.component.css'
    ],
})

export class ProfileComponent implements OnInit {

    user: User;

    constructor(
        private userSrv: UserService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initUser();
    }

    initUser() {
        this.userSrv
            .getCurrent()
            .then(user => this.user = user)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}
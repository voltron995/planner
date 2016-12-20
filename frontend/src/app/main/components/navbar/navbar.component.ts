import {Component, Input} from '@angular/core';
import {User} from "../../../users/models/user";
import {ResponseError} from "../../models/errors";
import {MessageService} from "../../services/message.service";
import {UserService} from "../../../users/services/user.service";

@Component({
    selector: 'navbar',
    templateUrl: 'navbar.component.html',
    styleUrls: [
        'navbar.component.css'
    ],
})
export class NavbarComponent {

    constructor(
        private usrSrv: UserService,
        private msgSrv: MessageService
    ) {}

    @Input()
    user: User;

    logOut() {
        this.usrSrv
            .logOut()
            .then(() => window.location.replace('/users/login'))
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail));
            });
    }

}

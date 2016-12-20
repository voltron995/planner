import {Component, OnInit} from '@angular/core';

// todo: do not import assets here, figure out how to compile them without import.
import '../../../../../public/css/styles.css'
import '../../../../../public/css/forms.css'
import '../../../../../node_modules/angular-calendar/dist/css/angular-calendar.css'
import '../../../../../node_modules/ng2-toasty/style-bootstrap.css'

import {UserService} from "../../../users/services/user.service";
import {User} from "../../../users/models/user";
import {ResponseError} from "../../models/errors";
import {MessageService} from "../../services/message.service";

@Component({
    selector: 'planner-app',
    templateUrl: 'app.component.html',
    styleUrls: [
        'app.component.css'
    ],
})
export class AppComponent implements OnInit {

    user: User;

    constructor(
        private userSrv: UserService,
        private msgSrv: MessageService,
    ) {}

    ngOnInit(): void {
        this.initUser();
    }

    private initUser() {
        this.userSrv
            .getCurrent()
            .then(user => this.user = user)
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}

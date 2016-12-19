import {Component, Input} from '@angular/core';
import {User} from "../../../users/models/user";
import {RequestService} from "../../services/request.service";

@Component({
    selector: 'navbar',
    templateUrl: 'navbar.component.html',
    styleUrls: [
        'navbar.component.css'
    ],
})
export class NavbarComponent {

    constructor(
        private requestSrv: RequestService
    ) {}

    @Input()
    user: User;

    public logout() {
        this.requestSrv
            .post('/users/logout', {})
        window.location.replace('/users/login')
    }

}

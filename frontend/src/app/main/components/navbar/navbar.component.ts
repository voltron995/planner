import {Component, Input} from '@angular/core';
import {User} from "../../../users/models/user";

@Component({
    selector: 'navbar',
    templateUrl: 'navbar.component.html',
    styleUrls: [
        'navbar.component.css'
    ],
})
export class NavbarComponent {

    @Input()
    user: User;

}

import {Component, OnInit} from '@angular/core';
import {User} from '../../users/models/user';
import {UserService} from '../../users/services/user.service';

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
        private userService: UserService,
    ) {}

    ngOnInit(): void {
        this.initUser();
    }

    initUser() {
        this.userService
            .getCurrent()
            .then(user => {
                this.user = user;
            });
    }

}

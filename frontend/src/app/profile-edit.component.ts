import {Component} from '@angular/core';
import {User} from './user';

@Component({
    selector: 'profile-edit',
    templateUrl: './profile-edit.component.html',
    styleUrls: [
        './profile-edit.component.css'
    ],

})

export class ProfileEditComponent {

    model = new User(13, 'vasya@exampe.com', 'vasya');
    submitted = false;

    onSubmit() {
        this.submitted = true;
    }

    // TODO: Remove this when we're done
    get diagnostic() {
        return JSON.stringify(this.model);
    }
}
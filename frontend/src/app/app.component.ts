import {Component} from '@angular/core';

// todo: do not import assets here, figure out how to compile them without import.
import '../../public/css/styles.css'
import '../../public/css/forms.css'
import '../../public/images/avatar-default.png'
import '../../public/images/logo.png'
import '../../public/images/sorry.jpg'
import '../../public/images/404.gif'

@Component({
    selector: 'planner-app',
    templateUrl: './app.component.html',
    styleUrls: [
        './app.component.css'
    ],
})
export class AppComponent {
    title = 'Welcome To Planner';
}

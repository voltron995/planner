import {Component} from '@angular/core';

// todo: do not import assets here, figure out how to compile them without import.
import '../../../../../public/css/styles.css'
import '../../../../../public/css/forms.css'

@Component({
    selector: 'planner-app',
    templateUrl: 'app.component.html',
    styleUrls: [
        'app.component.css'
    ],
})
export class AppComponent {}
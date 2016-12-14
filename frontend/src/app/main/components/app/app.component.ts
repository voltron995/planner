import {Component, OnInit, OnDestroy} from '@angular/core';

// todo: do not import assets here, figure out how to compile them without import.
import '../../../../../public/css/styles.css'
import '../../../../../public/css/forms.css'
import '../../../../../node_modules/angular-calendar/dist/css/angular-calendar.css'

@Component({
    selector: 'planner-app',
    templateUrl: 'app.component.html',
    styleUrls: [
        'app.component.css'
    ],
})
export class AppComponent implements OnInit, OnDestroy {
    ngOnInit(): void {
        console.log('app comp init');
    }

    ngOnDestroy(): void {
        console.log('app comp destroy');
    }

}

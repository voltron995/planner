import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {EventService} from '../../services/event.service';
import {Router} from '@angular/router'

@Component({
    selector: 'event-create-form',
    templateUrl: 'event-create.form.html',
    styleUrls: [
        'event-create.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class EventCreateForm implements OnInit {

    @Input()
    targets: any[];
    
    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private eventService: EventService,
        private router: Router
    ) {

    }

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          name: [''],
          target_id: [null],
          description: [''],
          start_time: [''],
          end_time: [''],
          color_primary: ['#bab2b7'],
          color_secondary: ['#d9d6d8'],
        });
    }

    onSubmit() {
        let values = this.form.value;
        if (!values.target_id) {
            delete values.target_id;
        }
        this.eventService
            .post(values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
        this.router.navigate(['/events'])
    }

}
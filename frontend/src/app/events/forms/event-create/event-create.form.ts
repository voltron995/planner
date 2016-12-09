import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {EventService} from '../../services/event.service';

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

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private eventService: EventService
    ) {

    }

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          name: [''],
          description: [''],
          start_time: [''],
          end_time: [''],
        });
    }

    onSubmit() {
        let values = this.form.value;
        console.log(values)
        this.eventService
            .post(values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
    }

}
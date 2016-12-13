import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {EventService} from '../../services/event.service';
import {Event} from '../../models/event';
import {Router} from '@angular/router'


@Component({
    selector: 'event-edit-form',
    templateUrl: 'event-edit.form.html',
    styleUrls: [
        'event-edit.form.css'
    ],
    providers: [
        FormBuilder
    ]
})

export class EventEditForm implements OnInit {

    @Input() event: Event;
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
          name: [this.event.name],
          description: [this.event.description],
          start_time: [this.event.startTime],
          end_time: [this.event.endTime],
        });
    }

    onSubmit() {
        let values = this.form.value;
        this.eventService
            .put(this.event.id, values)
            .then(profile => console.log(profile, 'success'))
            .catch(errors => console.log(errors, 'errors'));
        this.router.navigate(['/events', this.event.id])
    }

}
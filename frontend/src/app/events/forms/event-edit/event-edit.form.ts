import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {EventService} from '../../services/event.service';
import {Event} from '../../models/event';
import {Router} from '@angular/router'
import {MessageService} from "../../../main/services/message.service";
import {Target} from "../../../targets/models/targets";
import {ResponseError} from "../../../main/models/errors";


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

    @Input()
    event: Event;

    @Input()
    targets: Target[];

    form: FormGroup;

    constructor(
        private fb: FormBuilder,
        private eventSrv: EventService,
        private router: Router,
        private msgSrv: MessageService
    ) {}

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.form = this.fb.group({
          name: [this.event.name],
          target_id: [this.event.targetId],
          is_done: [this.event.isDone],
          description: [this.event.description],
          start_time: [this.event.startTime],
          end_time: [this.event.endTime],
          color_primary: [this.event.colorPrimary],
          color_secondary: [this.event.colorSecondary],
        });
    }

    onSubmit() {
        let values = this.form.value;
        if (!values.target_id) {
            delete values.target_id;
        }
        this.eventSrv
            .put(this.event.id, values)
            .then(event => {
                this.msgSrv.success(`Event ${this.event.name} successfully updated.`);
                this.router.navigate(['/events', this.event.id])
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}
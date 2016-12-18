import {Component, Input, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {EventService} from '../../services/event.service';
import {Router} from '@angular/router'
import {MessageService} from "../../../main/services/message.service";
import {Target} from "../../../targets/models/targets";
import {ResponseError} from "../../../main/models/errors";

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
        this.eventSrv
            .post(values)
            .then(event => {
                this.msgSrv.success(`Event ${event.name} successfully created.`);
                this.router.navigate(['/events'])
            })
            .catch((errors: ResponseError[]) => {
                errors.forEach(error => this.msgSrv.error(error.detail))
            });
    }

}
import {Component} from '@angular/core';
import {OnInit} from '@angular/core';

import {Event} from '../../models/event';
import {EventService} from '../../services/event.service';
import {Target} from '../../../targets/models/targets';
import {TargetService} from '../../../targets/services/target.service';


@Component({
    selector: 'events',
    templateUrl: 'events.component.html',
    styleUrls: [
        'events.component.css'
    ],
    providers: [
        EventService
    ]
})

export class EventsComponent implements OnInit {
    events: Event[];
    targets: Target[];
    selectedEvent: Event;

    constructor(private eventService: EventService, private targetService: TargetService) {
    }

    ngOnInit(): void {
        this.getEvents();
        this.getTargets();
    }

    getEvents(): void {
        this.eventService
            .list()
            .then(events => this.events = events);
    }

    getTargets(): void {
        this.targetService
            .list()
            .then(targets => this.targets = targets);
    }

    onSelect(event: Event): void {
        this.selectedEvent = event;
    }
}

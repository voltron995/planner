import {Component} from '@angular/core';
import {OnInit} from '@angular/core';

import {Event} from './event';
import {EventService} from './event.service';

import '../../public/css/styles.css'

@Component({
    selector: 'planner-app',
    templateUrl: './app.component.html',
    styleUrls: [
        './app.component.css'
    ],
    providers: [
        EventService
    ]
})

export class AppComponent implements OnInit {
    events: Event[];
    selectedEvent: Event;

    constructor(private eventService: EventService) {
    }

    ngOnInit(): void {
        this.getEvents();
    }

    getEvents(): void {
        this.eventService.getEvents().then(events => this.events = events);
    }

    onSelect(event: Event): void {
        this.selectedEvent = event;
    }
}

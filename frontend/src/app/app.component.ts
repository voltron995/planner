import {Component} from '@angular/core';
import {OnInit} from '@angular/core';

import {Event} from './event';
import {EventService} from './event.service';

// todo: do not import assets here, figure out how to compile them without import.
import '../../public/css/styles.css'
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

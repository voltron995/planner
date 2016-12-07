import { Component, Input } from '@angular/core';
import {Router} from '@angular/router'
import {
  startOfDay,
  subDays,
  addDays,
  endOfMonth,
  isSameDay,
  isSameMonth,
  addWeeks,
  subWeeks,
  addMonths,
  subMonths,
  addHours
} from 'date-fns';
import { Subject } from 'rxjs/Subject';
import {
  CalendarEvent,
  CalendarEventAction,
  CalendarEventTimesChangedEvent
} from 'angular-calendar'; // import should be from `angular-calendar` in your app
import {EventComponent} from "../event/event.component";
import {EventEditComponent} from "../event-edit/event-edit.component";


const colors: any = {
  red: {
    primary: '#ad2121',
    secondary: '#FAE3E3'
  },
  blue: {
    primary: '#1e90ff',
    secondary: '#D1E8FF'
  },
  yellow: {
    primary: '#e3bc08',
    secondary: '#FDF1BA'
  }
};

@Component({
  selector: 'calendar',
  styles: [`
    h3 {
      margin: 0;
    }
    .container {
      padding-bottom: 50px;
    }
  `],
    templateUrl: 'calendar.component.html',
})


export class CalendarComponent {

  constructor(private router: Router) {}

  @Input()
  eventsList: any[];

  view: string = 'month';

  viewDate: Date = new Date();

  actions: CalendarEventAction[] = [{
      label: '<i class="fa fa-fw fa-eye"></i>',
      onClick: ({event}: {event: CalendarEvent}): void => {      
      this.router.navigate(['/events', event.cssClass])
    }
  }, {
    label: '<i class="fa fa-fw fa-pencil"></i>',
    onClick: ({event}: {event: CalendarEvent}): void => {
        console.log(event)
        this.router.navigate(['/events', event.cssClass, 'edit'])
    }
  }, {
    label: '<i class="fa fa-fw fa-times"></i>',
    onClick: ({event}: {event: CalendarEvent}): void => {      
      console.log("delete event ", event.cssClass)
    }
  }];
  // cal-event-title

  refresh: Subject<any> = new Subject();

  events: CalendarEvent[] = [];

  activeDayIsOpen: boolean = true;

  increment(): void {

    const addFn: any = {
      day: addDays,
      week: addWeeks,
      month: addMonths
    }[this.view];

    this.viewDate = addFn(this.viewDate, 1);

  }

  decrement(): void {

    const subFn: any = {
      day: subDays,
      week: subWeeks,
      month: subMonths
    }[this.view];

    this.viewDate = subFn(this.viewDate, 1);

  }

  today(): void {
    this.viewDate = new Date();
  }

  dayClicked({date, events}: {date: Date, events: CalendarEvent[]}): void {

    if (isSameMonth(date, this.viewDate)) {
      if (
        (isSameDay(this.viewDate, date) && this.activeDayIsOpen === true) ||
        events.length === 0
      ) {
        this.activeDayIsOpen = false;
      } else {
        this.activeDayIsOpen = true;
        this.viewDate = date;
      }
    }
  }

  eventTimesChanged({event, newStart, newEnd}: CalendarEventTimesChangedEvent): void {
    event.start = newStart;
    event.end = newEnd;
    this.refresh.next();
  }

  ngAfterContentInit() {
      for (var event of this.eventsList) {
          var eventObj = {
              start: new Date(event.startTime),
              end: new Date(event.endTime),
              title: event.name,
              color: colors.yellow,
              actions: this.actions,
              cssClass: event.id
          }
          this.events.push(eventObj)
      };
  }
}
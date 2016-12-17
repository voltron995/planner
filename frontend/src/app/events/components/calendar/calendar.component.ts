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
} from 'angular-calendar';
import {EventService} from "../../services/event.service";
import {MessageService} from "../../../main/services/message.service"; // import should be from `angular-calendar` in your app


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
  },

  green: {
      primary: '#3d534b',
      secondary: '#77986f'
  },

  gray: {
    primary: '#bab2b7',
    secondary: '#d9d6d8'
  }

};

@Component({
    selector: 'calendar',
    styleUrls: [
        'calendar.component.css'
    ],
    templateUrl: 'calendar.component.html',
})


export class CalendarComponent {

  constructor(
      private router: Router,
      private eventSrv: EventService,
      private msgSrv: MessageService
  ) {}

  @Input()
  eventsList: any[];

  view: string = 'month';

  viewDate: Date = new Date();

    actions: CalendarEventAction[] = [
        // View
        {
            label: '<i class="fa fa-fw fa-eye"></i>',
            onClick: ({event}: {event: CalendarEvent}): void => {
                this.router.navigate(['/events', event.cssClass])
            }
        },
        // Edit
        {
            label: '<i class="fa fa-fw fa-pencil"></i>',
            onClick: ({event}: {event: CalendarEvent}): void => {
                this.router.navigate(['/events', event.cssClass, 'edit'])
            }
        },
        // Delete
        {
            label: '<i class="fa fa-fw fa-times"></i>',
            onClick: ({event}: {event: CalendarEvent}): void => {
                this.eventSrv
                    .delete(event.cssClass)
                    .then(() => {
                        let index = this.events.indexOf(event);
                        if (index !== -1) {
                            this.events.splice(index, 1);
                            this.refresh.next();
                        }
                        this.msgSrv.success(`Event ${event.title} successfully deleted.`);
                    });
                }
        }
    ];
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
          if (event.colorPrimary && event.colorSecondary) {
            var color_p: string = event.colorPrimary;
            var color_s: string = event.colorSecondary;
          } else {
            var color_p: string = "#bab2b7";
            var color_s: string = "#d9d6d8";
          }
          var eventObj = {
              start: new Date(event.startTime),
              end: new Date(event.endTime),
              title: event.name,
              color: {
                    primary: color_p,
                    secondary: color_s,
                },
              actions: this.actions,
              cssClass: event.id
          };
          this.events.push(eventObj)
      }
  }
}
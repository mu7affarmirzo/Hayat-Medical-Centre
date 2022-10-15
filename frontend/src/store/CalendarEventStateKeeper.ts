import {makeAutoObservable, runInAction} from "mobx";
import {CalendarEventApiStub} from "../repositories";
import {IEvent} from "../consts/types";

class CalendarEventStateKeeper {

    static _instance: CalendarEventStateKeeper;
    private readonly calendarEventApiStub: CalendarEventApiStub;

    static get instance() {
        if (!CalendarEventStateKeeper._instance) {
            CalendarEventStateKeeper._instance = new CalendarEventStateKeeper();
        }
        return CalendarEventStateKeeper._instance;
    }

    events: IEvent[] = [];

    eventsCopy: IEvent[] = [];

    constructor(
        calendarEventApiStub: CalendarEventApiStub = CalendarEventApiStub.instance
    ) {
        this.calendarEventApiStub = calendarEventApiStub;
        makeAutoObservable(this, {}, {autoBind: true});
    }

    addEvent (data: IEvent) {
        this.events.push(data)
    }

    filterEventByIds (ids: string[]) {
        this.eventsCopy = this.events.filter(item => ids.includes(item.doctorId || ''));
    }

    async findAllAppointments(): Promise<IEvent[]> {
        const appointments = await this.calendarEventApiStub.findAllAppointments();
        runInAction(() => {
            this.events = appointments.map((appointment) => {
                return {
                    id: appointment.id,
                    title: appointment.title,
                    doctorId: appointment.doctorId,
                    start: new Date(appointment.start),
                    end: new Date(appointment.end)
                }
            });
            this.eventsCopy = this.events;
        });
        return this.events;
    }
}

export default CalendarEventStateKeeper;
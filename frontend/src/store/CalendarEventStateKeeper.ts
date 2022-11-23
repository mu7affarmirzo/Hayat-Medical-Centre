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

    changeViewFunctions: Array<any> = [];

    constructor(
        calendarEventApiStub: CalendarEventApiStub = CalendarEventApiStub.instance
    ) {
        this.calendarEventApiStub = calendarEventApiStub;
        makeAutoObservable(this, {}, {autoBind: true});
    }

    addEvent (data: IEvent) {
        this.events.push(data)
        this.eventsCopy = this.events;
    }

    filterEventByDoctorId (id: string) {
        this.events.filter((item) => {
            console.log('doktoooooor', item);
        });
        return this.events.filter(item => item.doctorId === id);
    }

    filterEventByIds (ids: string[]) {
        this.eventsCopy = this.events.filter(item => ids.includes(item.doctorId || ''));
    }

    addViewAction (func) {
        this.changeViewFunctions.push(func)
    }

    async findAllAppointments(): Promise<IEvent[]> {
        const appointments = await this.calendarEventApiStub.findAllAppointments();
        console.log("appointments", appointments);

        runInAction(() => {
            if(this.events.length < appointments.length){
                this.events = appointments.map((appointment) => {
                    return {
                      id: 9,
                      //   id: appointment.id,
                      doctorId: appointment.doctorId,
                      title: appointment.name,
                      start: new Date(appointment.start_time),
                      end: new Date(appointment.end_time),
                    };
                });
            }
            this.eventsCopy = this.events;
        });
        return this.events;
    }
}

export default CalendarEventStateKeeper;
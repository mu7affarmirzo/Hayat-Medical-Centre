import {ApiClient} from "../utils";

import appointmentsList from "../repositories/data/appointments.json";
import {IAppointment} from "../consts/types";

export default class CalendarEventApiStub {
    /* Gen by NARA Studio */
    static _instance: CalendarEventApiStub;

    private readonly client = new ApiClient('/api/appointments');

    static get instance() {
        /* Gen by NARA Studio */
        if (!CalendarEventApiStub._instance) {
            CalendarEventApiStub._instance = new CalendarEventApiStub();
        }
        return CalendarEventApiStub._instance;
    }

    async findAllAppointments(): Promise<IAppointment[]> {
        /* Gen by NARA Studio */
        return appointmentsList ? appointmentsList as unknown as IAppointment[] : this.client.getArray<IAppointment>('/');
    }
}

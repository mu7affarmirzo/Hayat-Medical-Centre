import React, {useEffect, useMemo} from 'react';
import {Calendar, momentLocalizer} from 'react-big-calendar'
import moment from "moment";
import {observer, useLocalObservable} from "mobx-react-lite";
import {calendarComponent} from "./customComponents";
import {CalendarEventStateKeeper} from "../../store";
import CustomWeekView from "./customWeekView";
import CustomMonthView from "./customMonthView";
import CustomDayView from "./customDayView";

const CalendarMain = observer(() => {

    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const {eventsCopy, findAllAppointments} = calendarEventsStateKeeper;

    moment.locale("es-es", {
        week: {
            dow: 1 //Monday is the first day of the week.
        }
    });

    const mLocalizer = momentLocalizer(moment);

    const {components, views, messages} = useMemo(() => ({
        components: calendarComponent,
        views: {
            month: CustomMonthView,
            week: CustomWeekView,
            day: CustomDayView
        },
        messages: {
            today: 'Сегодня',
            month: 'месяц',
            week: 'неделя',
            day: 'день',
        },
    }), []);

    useEffect(() => {
        findAllAppointments().then();
    }, [findAllAppointments]);

    return (
        <>
            <Calendar
                // @ts-ignore
                components={components}
                events={eventsCopy}
                localizer={mLocalizer}
                startAccessor="end"
                endAccessor="end"
                // @ts-ignore
                views={views}
                className="calendar_block"
                messages={messages}
            />
        </>
    );
});

export default CalendarMain;
import React, {useEffect, useMemo} from 'react';
import {Calendar, momentLocalizer, Views} from 'react-big-calendar'
import moment from "moment";
import {observer} from "mobx-react-lite";
import {calendarComponent} from "./customComponents";
import CalendarEvents from "../../store/calendarEvents";



const CalendarMain = observer(() => {
    moment.locale("es-es", {
        week: {
            dow: 1 //Monday is the first day of the week.
        }
    });

    const mLocalizer = momentLocalizer(moment);

    console.log(CalendarEvents.eventsCopy)

    const {components, views, messages, events} = useMemo(() => ({
        components: calendarComponent,
        views: { month: true, week: true, day: true},
        messages: {
            today: 'Сегодня',
            month: 'месяц',
            week: 'неделя',
            day: 'день',
        },

        events: CalendarEvents.eventsCopy
    }),[]);
    return (
        <>

            <Calendar
                // @ts-ignore
                components={components}
                events={events}
                localizer={mLocalizer}
                startAccessor="end"
                endAccessor="end"
                views={views}
                className="calendar_block"
                messages={messages}

            />
        </>
    );
});

export default CalendarMain;
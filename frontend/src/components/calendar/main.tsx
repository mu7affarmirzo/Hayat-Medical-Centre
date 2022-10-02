import React, {useMemo} from 'react';
import {Calendar, momentLocalizer, Views} from 'react-big-calendar'
import moment from "moment";
import {calendarComponent} from "./customComponents";



const CalendarMain = () => {
    moment.locale("es-es", {
        week: {
            dow: 1 //Monday is the first day of the week.
        }
    });

    const mLocalizer = momentLocalizer(moment);

    const {components, views, messages} = useMemo(() => ({
        components: calendarComponent,
        views: { month: true, week: true, day: true},
        messages: {
            today: 'Сегодня',
            month: 'месяц',
            week: 'неделя',
            day: 'день',
        }
    }),[]);

    // const formats = useMemo(() => ({
    //     // dateFormat: 'dd',
    //
    //     dayFormat: (date:any, localizer) =>
    //         localizer.format(date, 'DDD', "ru"),
    //     //
    //     dayRangeHeaderFormat: ({ start, end }, culture, localizer) =>
    //         localizer.format(start, { date: 'short' }, culture) + ' — ' +
    //         localizer.format(end, { date: 'short' }, culture)
    // }), [])

    return (
        <>

            <Calendar
                // @ts-ignore
                components={components}
                events={[]}
                localizer={mLocalizer}
                startAccessor="end"
                endAccessor="end"
                views={views}
                className="calendar_block"
                messages={messages}
                // formats={formats}

            />
        </>
    );
};

export default CalendarMain;
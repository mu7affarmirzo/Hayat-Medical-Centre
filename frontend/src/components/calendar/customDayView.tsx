import React, {useMemo} from "react";
import {useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";
import Day from "react-big-calendar/lib/Day";
import PropTypes from "prop-types";
import {Navigate} from "react-big-calendar";
import {Typography} from "@mui/material";

export default function CustomDayView({
                                          date,
                                          localizer,
                                          max = localizer.endOf(new Date(), 'day'),
                                          min = localizer.startOf(new Date(), 'day'),
                                          scrollToTime = localizer.startOf(new Date(), 'time'),
                                          ...props
                                      }) {
    const currRange = useMemo(
        () => CustomDayView.range(date, {localizer}),
        [date, localizer]
    )
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);
    const {selectedDoctors} = doctorStateKeeper;
    return (
        <div
            style={{
                width: `100%`,
                height: '100%',
                display: 'flex',
                overflow: 'scroll',
            }}>
            {
                selectedDoctors
                    .map((doctor) => (
                        <div
                            key={doctor.id}
                            style={{
                                width: '100%',
                                borderLeft: 1,
                                borderRight: 1,
                                borderLeftStyle: 'solid',
                                borderRightStyle: 'solid',
                                borderLeftColor: '#000',
                                borderRightColor: '#000',
                            }}>
                            <Typography
                                variant={'h5'}
                                align={'center'}
                                style={{
                                    background: '#64B6F7',
                                }}
                            >
                                {doctor.fullName}
                            </Typography>
                            <Day
                                date={date}
                                eventOffset={15}
                                localizer={localizer}
                                max={max}
                                min={min}
                                range={currRange}
                                scrollToTime={scrollToTime}
                                {...props}
                            />
                        </div>
                    ))
            }
        </div>
    )
}

CustomDayView.propTypes = {
    date: PropTypes.instanceOf(Date).isRequired,
    localizer: PropTypes.object,
    max: PropTypes.instanceOf(Date),
    min: PropTypes.instanceOf(Date),
    scrollToTime: PropTypes.instanceOf(Date),
}

CustomDayView.range = (date, {localizer}) => {
    const start = localizer.add(date, -3, 'day')
    const end = localizer.add(start, 6, 'day')

    let current = start
    const range = []

    while (localizer.lte(current, end, 'day')) {
        // @ts-ignore
        range.push(current)
        current = localizer.add(current, 1, 'day')
    }

    return range
}

CustomDayView.navigate = (date, action, {localizer}) => {
    switch (action) {
        case Navigate.PREVIOUS:
            return localizer.add(date, -3, 'day')

        case Navigate.NEXT:
            return localizer.add(date, 3, 'day')

        default:
            return date
    }
}

CustomDayView.title = (date, {localizer}) => {
    const [start, ...rest] = CustomDayView.range(date, {localizer})
    return localizer.format({start, end: rest.pop()}, 'dayRangeHeaderFormat')
}
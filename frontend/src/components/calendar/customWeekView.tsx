import React, {useMemo} from "react";
import {useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";
import Week from "react-big-calendar/lib/Week";
import PropTypes from "prop-types";
import {Navigate} from "react-big-calendar";
import {Typography} from "@mui/material";
import moment from "moment";
import Month from "react-big-calendar/lib/Month";
import CustomViewWrapper from "./customViewWrapper";

export default function CustomWeekView({
                                           date,
                                           localizer,
                                           max = localizer.endOf(new Date(), 'day'),
                                           min = localizer.startOf(new Date(), 'day'),
                                           scrollToTime = localizer.startOf(new Date(), 'day'),
                                           ...props
                                       }) {
    const currRange = useMemo(
        () => CustomWeekView.range(date, {localizer}),
        [date, localizer]
    )
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);
    const {selectedDoctors} = doctorStateKeeper;
    return (
        <CustomViewWrapper>
            <Week
                date={date}
                eventOffset={15}
                localizer={localizer}
                max={max}
                min={min}
                range={currRange}
                scrollToTime={scrollToTime}
                {...props}
            />
        </CustomViewWrapper>
    )
}

CustomWeekView.propTypes = {
    date: PropTypes.instanceOf(Date).isRequired,
    localizer: PropTypes.object,
    max: PropTypes.instanceOf(Date),
    min: PropTypes.instanceOf(Date),
    scrollToTime: PropTypes.instanceOf(Date),
}

CustomWeekView.range = (date, {localizer}) => {
    const start = moment(date).startOf('week');
    const end = moment(date).endOf('week');

    let current = start
    const range = []

    while (localizer.lte(current, end, 'day')) {
        // @ts-ignore
        range.push(current)
        current = localizer.add(current, 1, 'day')
    }

    return range
}

CustomWeekView.navigate = (date, action, {localizer}) => {
    switch (action) {
        case Navigate.PREVIOUS:
            return localizer.add(date, -3, 'day')

        case Navigate.NEXT:
            return localizer.add(date, 3, 'day')

        default:
            return date
    }
}

CustomWeekView.title = (date, {localizer}) => {
    const [start, ...rest] = CustomWeekView.range(date, {localizer})
    return localizer.format({start, end: rest.pop()}, 'dayRangeHeaderFormat')
}
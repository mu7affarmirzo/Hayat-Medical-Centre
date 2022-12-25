import React, {useEffect} from 'react';
import {Typography} from "@mui/material";
import {useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";
import { CalendarEventStateKeeper } from '../../store';

const CustomViewWrapper = ({children}) => {
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);
    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const { selectedDoctors } = doctorStateKeeper;
    const { calendarView } = calendarEventsStateKeeper;

    useEffect(() => {
        document.querySelectorAll("#container_calendar #calendar_title").forEach((item) => {
            if(item){
                const { doctor, specialty } = selectedDoctors[calendarView];
                item.textContent = `${specialty?.map(item => item.name).join()} - ${doctor.f_name ?? doctor.username}`
            }
        })
    }, [selectedDoctors, calendarView])

    return (
        <div
            id="container_calendar"
            style={{
                width: '100%',
                height: '100%',
                overflow: 'auto',
            }}
        >
            <Typography
                id="calendar_title"
                variant={'h5'}
                sx={{
                    backgroundColor: '#64B6F7',
                    fontSize: "16px",
                    lineHeight: "28px",
                    letterSpacing: "0.15px",
                    color: "#000000",
                    textAlign: "center"
                }}
            >

            </Typography>
            {children}
        </div>
    );
};

export default CustomViewWrapper;
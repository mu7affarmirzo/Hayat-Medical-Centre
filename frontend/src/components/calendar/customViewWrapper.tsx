import React, {useEffect} from 'react';
import {Typography} from "@mui/material";
import {useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";

const CustomViewWrapper = ({children}) => {
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);
    const {selectedDoctors, setSelectedDoctor} = doctorStateKeeper;
    console.log(selectedDoctors, "selectedDoctors")

    useEffect(() => {
        document.querySelectorAll("#container_calendar #calendar_title").forEach((item, index) => {
            if(item){
                const { f_name, speciality } = selectedDoctors[index];
                // item.textContent = `${speciality.name} - ${f_name}`
            }
        })
    }, [selectedDoctors])

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
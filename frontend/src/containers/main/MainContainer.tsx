import React, {useState} from 'react';
import { MainView } from "../../views";
import DoctorsList from "../../repositories/doctors.json"
import SpecialitiesList from "../../repositories/specialities.json"
import {IDoctors} from "../../consts/types";
import styles from "../../views/main/index.module.scss"
import CalendarEvents from "../../store/calendarEvents";

const MainContainer = () => {
    const [selectData, setSelectData] = useState<string>('');
    const [doctorsData, setDoctorsData] = useState<Array<IDoctors>>(DoctorsList);
    const [selectedDoctor, setSelectedDoctor] = useState<Array<string>>([]);

    const changeSpecialty = (id: string) => {
        let filteredData;

        if(id === "all"){
            filteredData = DoctorsList;
        }else{
            filteredData = DoctorsList.filter(item => item.speciality.id === id);
        }

        setDoctorsData(filteredData);
    }

    const selectDoctor = (e: React.MouseEvent<HTMLElement>, data: IDoctors) => {
        let parentElem = e.currentTarget.closest(".doctors_table_row");

        CalendarEvents.filterEventById(data.id);

        if(parentElem && parentElem.classList.contains(styles.selected)){
            setSelectedDoctor(prev => prev.filter(item => item !== data.id))
        }else{
            setSelectedDoctor(prev => [...prev, data.id])
        }
    }

    return (
        <>
            <MainView
                selectData={selectData}
                setSelectData={setSelectData}
                doctors={doctorsData}
                specialities={SpecialitiesList}
                changeSpecialty={changeSpecialty}
                selectDoctor={selectDoctor}
                selectedDoctor={selectedDoctor}
            />
        </>
    );
};

export default MainContainer;
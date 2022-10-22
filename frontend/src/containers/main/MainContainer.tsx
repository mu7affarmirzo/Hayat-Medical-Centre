import React, {useEffect, useState} from 'react';
import {MainView} from "../../views";
import {IDoctor} from "../../consts/types";
import styles from "../../views/main/index.module.scss"
import {CalendarEventStateKeeper} from "../../store";
import {observer, useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";
import {SpecialityStateKeeper} from "../../store";

const MainContainer = observer(() => {

    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const specialityStateKeeper = useLocalObservable(() => SpecialityStateKeeper.instance);
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);

    const {filterEventByIds} = calendarEventsStateKeeper;
    const {specialities, findAllSpecialties} = specialityStateKeeper;
    const {doctors, findAllDoctors, selectedDoctors, setSelectedDoctors} = doctorStateKeeper;

    const [selectData, setSelectData] = useState<string>('');
    const [doctorsData, setDoctorsData] = useState<Array<IDoctor>>(doctors);

    useEffect(() => {
        filterEventByIds(selectedDoctors.map((doctor) => doctor.id));
    }, [selectedDoctors]);

    useEffect(() => {
        findAllSpecialties()
            .then(() => {
            findAllDoctors()
                .then((items) => {
                    setDoctorsData(items);

                });
        });
    }, [findAllSpecialties, findAllDoctors]);

    const changeSpecialty = (id: string) => {
        let filteredData;

        if (id === "all") {
            filteredData = doctors;
        } else {
            filteredData = doctors.filter(item => item.speciality.id === id);
        }

        setDoctorsData(filteredData);
    }

    const handleSelectDoctor = (e: React.MouseEvent<HTMLElement> | React.ChangeEvent<HTMLInputElement>, data: IDoctor) => {
        let parentElem = e.currentTarget.closest(".doctors_table_row");

        if (parentElem && parentElem.classList.contains(styles.selected)) {
            setSelectedDoctors(selectedDoctors.filter(item => item.id !== data.id))
        } else {
            setSelectedDoctors([...selectedDoctors, data])
        }
    }

    return (
        <>
            <MainView
                selectData={selectData}
                setSelectData={setSelectData}
                doctors={doctorsData}
                specialities={specialities}
                changeSpecialty={changeSpecialty}
                onSelectDoctor={handleSelectDoctor}
                selectedDoctors={selectedDoctors}
            />
        </>
    );
});

export default MainContainer;
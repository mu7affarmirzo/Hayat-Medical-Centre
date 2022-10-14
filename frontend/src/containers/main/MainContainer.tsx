import React, {useEffect, useState} from 'react';
import {MainView} from "../../views";
import {IDoctor} from "../../consts/types";
import styles from "../../views/main/index.module.scss"
import {CalendarEventStateKeeper} from "../../store";
import {observer, useLocalObservable} from "mobx-react-lite";
import DoctorStateKeeper from "../../store/DoctorStateKeeper";
import SpecialityStateKeeper from "../../store/SpecialityStateKeeper";

const MainContainer = observer(() => {

    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const specialityStateKeeper = useLocalObservable(() => SpecialityStateKeeper.instance);
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);

    const {filterEventById} = calendarEventsStateKeeper;
    const {specialities, findAllSpecialties} = specialityStateKeeper;
    const {doctors, findAllDoctors} = doctorStateKeeper;

    const [selectData, setSelectData] = useState<string>('');
    const [doctorsData, setDoctorsData] = useState<Array<IDoctor>>(doctors);
    const [selectedDoctor, setSelectedDoctor] = useState<Array<string>>([]);

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

        filterEventById(data.id);

        if (parentElem && parentElem.classList.contains(styles.selected)) {
            setSelectedDoctor(prev => prev.filter(item => item !== data.id))
        } else {
            setSelectedDoctor(prev => [...prev, data.id])
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
                selectedDoctor={selectedDoctor}
            />
        </>
    );
});

export default MainContainer;
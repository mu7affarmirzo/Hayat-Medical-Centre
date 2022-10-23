import React, {useEffect, useState} from 'react';
import {MainView} from "../../views";
import {IDoctor} from "../../consts/types";
import styles from "../../views/main/index.module.scss"
import {CalendarEventStateKeeper} from "../../store";
import {observer, useLocalObservable} from "mobx-react-lite";
import {DoctorStateKeeper} from "../../store";
import {SpecialityStateKeeper} from "../../store";

const MainContainer = observer(() => {

    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const specialityStateKeeper = useLocalObservable(() => SpecialityStateKeeper.instance);
    const doctorStateKeeper = useLocalObservable(() => DoctorStateKeeper.instance);

    const {filterEventByIds} = calendarEventsStateKeeper;
    const {specialitiesCopy, findAllSpecialties, searchByName} = specialityStateKeeper;
    const {doctorsCopy, findAllDoctors, selectedDoctors, setSelectedDoctors, searchDoctor} = doctorStateKeeper;

    const [selectData, setSelectData] = useState<string>('');
    const [doctorsData, setDoctorsData] = useState<Array<IDoctor>>(doctorsCopy);
    const [searchInputsValue, setSearchInputs] = useState<{specialities: string, doctors: string}>({specialities: "", doctors: ""});

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
            filteredData = doctorsCopy;
        } else {
            filteredData = doctorsCopy.filter(item => item.speciality.id === id);
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

    const searchInputsHandler = (type: string, value: string) => {
        setSearchInputs(prev => ({...prev, [type]: value}))
        if(type === "specialities"){
            searchByName(value)
        }else if(type === "doctors") {
            searchDoctor(value)
        }
    }

    return (
        <>
            <MainView
                selectData={selectData}
                setSelectData={setSelectData}
                doctors={doctorsCopy}
                specialities={specialitiesCopy}
                changeSpecialty={changeSpecialty}
                onSelectDoctor={handleSelectDoctor}
                selectedDoctors={selectedDoctors}
                searchInputsValue={searchInputsValue}
                searchInputsHandler={searchInputsHandler}
            />
        </>
    );
});

export default MainContainer;
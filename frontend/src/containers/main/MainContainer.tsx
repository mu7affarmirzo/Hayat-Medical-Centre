import React, { useEffect, useState } from "react";
import { MainView } from "../../views";
import { IDoc } from "../../consts/types";
import styles from "../../views/main/index.module.scss";
import {
    AuthorizationStateKeeper,
    CalendarEventStateKeeper,
} from "../../store";
import { observer, useLocalObservable } from "mobx-react-lite";
import { DoctorStateKeeper } from "../../store";
import { SpecialityStateKeeper } from "../../store";
import BranchesStateKeeper from "../../store/BranchesStateKeeper";
import request from "../../utils/request";

const MainContainer = observer(() => {
    const calendarEventsStateKeeper = useLocalObservable(
        () => CalendarEventStateKeeper.instance
    );
    const specialityStateKeeper = useLocalObservable(
        () => SpecialityStateKeeper.instance
    );
    const doctorStateKeeper = useLocalObservable(
        () => DoctorStateKeeper.instance
    );
    const branchesStateKeeper = useLocalObservable(
        () => BranchesStateKeeper.instance
    );
    const { filterEventByIds } = calendarEventsStateKeeper;
    const { specialitiesCopy, findAllSpecialties, searchByName, setSpecialist } =
        specialityStateKeeper;
    const {
        doctorsCopy,
        findAllDoctors,
        selectedDoctors,
        setSelectedDoctors,
        searchDoctor,
    } = doctorStateKeeper;
    const { findAllBranches, branchesCopy } = branchesStateKeeper;
    const [selectData, setSelectData] = useState<string>("");
    const [doctorsData, setDoctorsData] = useState<Array<IDoc>>(doctorsCopy);
    const authorizationStateKeeper = useLocalObservable(
        () => AuthorizationStateKeeper.instance
    );
    const token = authorizationStateKeeper.token;

    const [searchInputsValue, setSearchInputs] = useState<{
        specialities: string;
        doctors: string;
    }>({ specialities: "", doctors: "" });

    useEffect(() => {
        filterEventByIds(selectedDoctors.map((doctor) => String(doctor.doctor.id)));
    }, [selectedDoctors]);

    useEffect(() => {
        findAllBranches().then(() => {
            findAllSpecialties().then(() => {
                findAllDoctors().then((items) => {
                    setDoctorsData(items);
                });
            });
        });
    }, [findAllSpecialties, findAllDoctors, findAllBranches]);
    const changeSpecialty = (id: string) => {
        let filteredData;
        if (id === "all") {
            filteredData = doctorsCopy;
        } else {
            filteredData = doctorsCopy.filter((item) => {
                if (Object.values(item.specialty)[0]) {
                    const specCopy: any = Object.values(item.specialty)[0]
                    return specCopy.id === parseInt(id)
                }
            });
        }
        setDoctorsData(filteredData);
    };
    const handleSelectDoctor = (
        e: React.MouseEvent<HTMLElement> | React.ChangeEvent<HTMLInputElement>,
        data: IDoc
    ) => {
        let parentElem = e.currentTarget.closest(".doctors_table_row");

        if (parentElem && parentElem.classList.contains(styles.selected)) {
            setSelectedDoctors(selectedDoctors.filter((item) => item.doctor.id !== data.doctor.id));
        } else {
            setSelectedDoctors([...selectedDoctors, data]);
        }

    };

    const handleChangeBranch = (id: string) => {
        setSelectData(id)
        const headers = {
            headers: {
                Authorization: "Bearer " + JSON.parse(token).access,
            },
        }
        request
            .get(
                `https://back.dev-hayat.uz/api/v1/organizations/branches/doctors/${id}`,
                headers
        )
            .then((res) => {
                setDoctorsData(res.data)
            })
            .catch((err) => console.log(err));
        request
            .get(
                `https://back.dev-hayat.uz/api/v1/organizations/branches/specialty/${id}`,
                headers
            )
            .then((res) => {
                setSpecialist(res.data)
            })
            .catch((err) => console.log(err));
    };

    const searchInputsHandler = (type: string, value: string) => {
        setSearchInputs((prev) => ({ ...prev, [type]: value }));
        if (type === "specialities") {
            searchByName(value);
        } else if (type === "doctors") {
            searchDoctor(value);
        }
    };

    return (
        <>
            <MainView
                selectData={selectData}
                setSelectData={setSelectData}
                doctors={doctorsData}
                specialities={specialitiesCopy}
                branchesCopy={branchesCopy}
                changeSpecialty={changeSpecialty}
                onSelectDoctor={handleSelectDoctor}
                selectedDoctors={selectedDoctors}
                searchInputsValue={searchInputsValue}
                searchInputsHandler={searchInputsHandler}
                handleChangeBranch={handleChangeBranch}
            />
        </>
    );
});

export default MainContainer;

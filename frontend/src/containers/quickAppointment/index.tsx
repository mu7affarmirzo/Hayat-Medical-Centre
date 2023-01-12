import React, { useEffect, useState } from "react";
import classes from "./quickAppointment.module.scss";
import CancelOutlinedIcon from "@mui/icons-material/CancelOutlined";
import { Button } from "@mui/material";
import { IDoc } from "../../consts/types";
import { DoctorStateKeeper } from "../../store";
import { useLocalObservable } from "mobx-react-lite";
import BpCheckbox from "../../components/BpCheckbox";
import { Link } from "react-router-dom";

const QuickAppointment = ({ close }) => {
    const doctorStateKeeper = useLocalObservable(
        () => DoctorStateKeeper.instance
    );

    const {
        doctorsCopy,
        findAllDoctors,
        selectedDoctors,
        setSelectedDoctors,
    } = doctorStateKeeper;
    const [doctorsData, setDoctorsData] = useState<Array<IDoc>>(doctorsCopy);
    const [selectedDoctorData, setSelectedDoctorData] = useState<IDoc[]>([])
    useEffect(() => {
        findAllDoctors().then((items) => {
            setDoctorsData(items);
        });
    }, [findAllDoctors]);

    const onSelectDoctor = (
        e: React.MouseEvent<HTMLElement> | React.ChangeEvent<HTMLInputElement>,
        data: IDoc
    ) => {
        let parentElem = e.currentTarget.closest(".doctors_table_row");

        if (parentElem && parentElem.classList.contains(classes.selected)) {
            setSelectedDoctors(
                selectedDoctors.filter((item) => item.doctor.id !== data.doctor.id)
            );
            setSelectedDoctorData(
                selectedDoctors.filter((item) => item.doctor.id !== data.doctor.id)
            );
        } else {
            setSelectedDoctors([...selectedDoctors, data]);
            setSelectedDoctorData([...selectedDoctors, data]);
        }
    };

    return (
        <div className={classes.quickAppointment}>
            <div className={classes.header}>
                <h5 className={classes.title}>Быстрая запись</h5>
                <button className={classes.close}>
                    <CancelOutlinedIcon />
                </button>
            </div>
            <div className={`${classes.table_doctors} ${classes.custom_scrollbar}`}>
                {doctorsData.map(
                    (doctor: IDoc) =>
                        doctor.doctor && (
                            <div
                                onClick={(e) => onSelectDoctor(e, doctor)}
                                key={doctor.doctor.id}
                                className={`doctors_table_row ${classes.row} ${selectedDoctorData
                                    .map((doctor) => doctor.doctor.id)
                                    .includes(doctor.doctor.id)
                                    ? classes.selected
                                    : ""
                                    }`}
                            // style={{backgroundColor: item.color}}
                            >
                                <div className={classes.cell}>
                                    <label className={classes.checkbox_block}>
                                        <input
                                            type="checkbox"
                                            checked={selectedDoctors
                                                .map((doctor) => doctor.id)
                                                .includes(doctor.id)}
                                            onChange={(e) => onSelectDoctor(e, doctor)}
                                        />
                                        <div className={classes.box}></div>
                                    </label>
                                </div>
                                <div className={classes.cell}>
                                    {doctor.doctor?.f_name ?? doctor.doctor.username}
                                </div>
                                <div className={classes.cell}>
                                    {doctor.specialty?.map((item) => item.name).join()}
                                </div>
                                <div className={classes.cell}>
                                    {doctor.doctor.phone_number}
                                </div>
                                <div className={classes.cell}>
                                    <div
                                        className={`${classes.status_block} ${doctor?.is_at_work ? "" : classes.not_active
                                            }`}
                                    ></div>
                                </div>
                            </div>
                        )
                )}
            </div>
            <div className={classes.actions}>
                <Link to="/createNote">
                    <Button onClick={close} disabled={selectedDoctorData.length > 0 ? false : true} variant="contained">OK</Button>
                </Link>
                <Button onClick={close} className={classes.secondary}>
                    Отмена
                </Button>
            </div >
        </div >
    );
};

export default QuickAppointment;

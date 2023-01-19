import {
    Button,
    Checkbox,
    FormControl,
    FormControlLabel,
    Radio,
    RadioGroup,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import SearchPanel from "../../components/SearchPanel";
import classes from "./mergePatient.module.scss";
import { ReactComponent as Dataicon } from "../../assets/img/data.svg";
import { ReactComponent as TickIcon } from "../../assets/img/tick-circle.svg";
import { IMergePatient, IPatient } from "../../consts/types";
import { useLocalObservable } from "mobx-react-lite";
import { PatientStateKeeper } from "../../store";

const MergePatientsView = () => {
    const patientStateKeeper = useLocalObservable(
        () => PatientStateKeeper.instance
    );

    const [patients, setPatients] = useState<IPatient[]>([]);
    const [selectedPatient, setSelectedpatient] = useState<IMergePatient[]>([]);
    useEffect(() => {
        patientStateKeeper.findAllPatients().then((res) => setPatients(res));
    }, []);

    const onSelectPatient = (id: number) => {
        const patient = selectedPatient;
        const isAdded = patient.filter((item) => item.id === id);

        if (!isAdded.length) {
            patient.push({ id, is_base: false });
            setSelectedpatient(patient);
        } else {
            const index = patient.findIndex((obj) => obj.id === id);
            patient.splice(index, 1);
            setSelectedpatient(patient);
    }
    };

    const handleMakeBaseAccount = (id) => {
        if (selectedPatient.length > 0) {
            const updatedPatients = [...selectedPatient];
            const baseUser = updatedPatients.findIndex((obj) => obj.id === id);
            console.log('selectedPatient')
            updatedPatients[baseUser].is_base = true;
            setSelectedpatient(updatedPatients);
        } else {
            setSelectedpatient([{ id, is_base: true }]);
        }

    };

    const mergeHandler = () => {
        return console.log("selectedPatient", selectedPatient);
        patientStateKeeper.mergePatients({ patients: selectedPatient });
    };

    return (
        <div className={classes.wrapper}>
            <SearchPanel />
            <div className={`${classes.clonedPatientsWrapper} ${classes.table}`}>
                <table className={classes.tableBody}>
                    <thead>
                        <th></th>
                        <th>Oсновной</th>
                        <th>Фамилия</th>
                        <th>Имя</th>
                        <th>Отчество</th>
                        <th>Дата рождения</th>
                        <th>Пол</th>
                        <th>Эл. почта</th>
                        <th>Моб. телефон</th>
                        <th>Адрес </th>
                    </thead>
                    {patients.map((patient) => (
                        <tr>
                            <td style={{ width: "63px" }}>
                                <Checkbox
                                    value={patient.id}
                                    onChange={() => onSelectPatient(patient.id)}
                                    inputProps={{
                                        "aria-label": "Checkbox A",
                                    }}
                                />
                            </td>
                            <td style={{ textAlign: "center" }}>
                                <input
                                    type="radio"
                                    onChange={e => handleMakeBaseAccount(parseInt(e.target.value))}
                                    value={patient.id}
                                    name="is_base"
                                />
                            </td>
                            <td>{patient.l_name}</td>
                            <td>{patient.f_name}</td>
                            <td>{patient.mid_name}</td>
                            <td>{patient.date_of_birth}</td>
                            <td>{patient.sex}</td>
                            <td>{patient.email}</td>
                            <td>{patient.mobile_phone_number}</td>
                            <td>{patient.address}</td>
                        </tr>
                    ))}
                </table>
            </div>
            <FormControl className={classes.sortingActions}>
                <RadioGroup
                    row
                    className={classes.radioWrapper}
                    aria-labelledby="demo-row-radio-buttons-group-label"
                    name="row-radio-buttons-group"
                >
                    <FormControlLabel
                        value="none"
                        control={<Radio />}
                        label="Нечего не делать с лишними пациентами"
                    />
                    <FormControlLabel
                        value="off"
                        control={<Radio />}
                        label="Отключить лишних пациентов"
                    />
                    <FormControlLabel
                        value="delete"
                        control={<Radio />}
                        label="Удалить лишних пациентов"
                    />
                </RadioGroup>
                <Button size="large" variant="contained" onClick={mergeHandler}>
                    Добавить к слиянию
                </Button>
            </FormControl>
            <h5 className={classes.tableHeading}>
                Список пациентов, которые будут объединены
            </h5>
            <div className={`${classes.mergedPatientsWrapper} ${classes.table}`}>
                <table className={classes.tableBody}>
                    <thead>
                        <th></th>
                        <th>Фамилия</th>
                        <th>Имя</th>
                        <th>Отчество</th>
                        <th>Дата рождения</th>
                        <th>Пол</th>
                        <th>Эл. почта</th>
                        <th>Моб. телефон</th>
                        <th>Адрес </th>
                    </thead>
                    <tr>
                        <td></td>
                        <td>
                            {
                                "Однозначно, стремящиеся вытеснить традиционное производство, нанотехнологии представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть описаны максимально подробно."
                            }
                        </td>
                        <td>{"Невролог "}</td>
                        <td>{"нет данных"}</td>
                        <td>{"09.08.2022"}</td>
                        <td>{"09.08.2022"}</td>
                        <td>{"09.08.2022"}</td>
                        <td>{"15:23"}</td>
                        <td>{"15:33"}</td>
                    </tr>
                </table>
            </div>
            <div className={classes.actions}>
                <Button
                    size="large"
                    variant="outlined"
                    className={classes.secondaryButton}
                    color="secondary"
                >
                    <TickIcon />
                    Отметить пациента, как основного
                </Button>
                <Button size="large" variant="contained" color="primary">
                    <Dataicon />
                    Выполнить слияние
                </Button>
            </div>
        </div>
    );
};

export default MergePatientsView;

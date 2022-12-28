import {
    Button,
    Checkbox,
    FormControl,
    FormControlLabel,
    Radio,
    RadioGroup,
} from "@mui/material";
import React from "react";
import SearchPanel from "../../components/SearchPanel";
import classes from "./mergePatient.module.scss";
import { ReactComponent as Dataicon } from "../../assets/img/data.svg";
import { ReactComponent as TickIcon } from "../../assets/img/tick-circle.svg";
import patients from "../../repositories/data/patients.json";

const MergePatientsView = () => {
    return (
        <div className={classes.wrapper}>
            <SearchPanel />
            <div className={`${classes.clonedPatientsWrapper} ${classes.table}`}>
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
                    {patients.splice(0, 3).map((patient) => (
                        <tr>
                            <td style={{ width: "63px" }}>
                                <Checkbox
                                    value={patient.firstName}
                                    inputProps={{
                                        "aria-label": "Checkbox A",
                                    }}
                                />
                            </td>
                            <td>{patient.firstName}</td>
                            <td>{patient.lastName}</td>
                            <td>{patient.middleName}</td>
                            <td>{patient.dob}</td>
                            <td>{"male"}</td>
                            <td>{patient.email}</td>
                            <td>{patient.mobilePhoneNumber}</td>
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
                <Button size="large" variant="contained">
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

import React from "react";
import {
    Button,
    FormControl,
    Input,
    InputAdornment,
    InputLabel,
    MenuItem,
    Select,
    TextField,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import { ReactComponent as Export } from "../../assets/img/excelDownload.svg";
import classes from "../RegistryVisits/registeryVisits.module.scss";
import payment from "../../repositories/data/visits.json";

const RegisteredAccounts = () => {
    return (
        <div className={classes.wrapper}>
            <div className={classes.actions}>
                <div className={classes.actionItem}>
                    <TextField label="Дата от:" />
                </div>
                <div className={classes.actionItem}>
                    <TextField className={classes.actionItem} label="Дата до:" />
                </div>
                <div className={classes.actionItem}>
                    <FormControl className={classes.actionItem}>
                        <InputLabel id="demo-simple-select-label">Филиал:</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Филиал:"
                        >
                            <MenuItem value={"Головной"}>Головной</MenuItem>
                        </Select>
                    </FormControl>
                </div>
                <div className={classes.actionItem}>
                    <FormControl className={classes.actionItem}>
                        <InputLabel id="demo-simple-select-label">Тип приёма:</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Тип приёма:"
                        >
                            <MenuItem value={"Все"}>Все</MenuItem>
                        </Select>
                    </FormControl>
                </div>
                <div className={classes.actionItem}>
                    <TextField className={classes.actionItem} label="ID клиента" />
                </div>

                <Button className={classes.actionButton}>
                    <Export />
                    <span>
                        Экспорть <br />в Excel
                    </span>
                </Button>
            </div>
            <div className={classes.tableWrapper}>
                <FormControl className={classes.searchbox} variant="standard">
                    <Input
                        placeholder="Поместите сюда заголовок колонки для группировки по этой колонке."
                        id="input-with-icon-adornment"
                        endAdornment={
                            <InputAdornment position="end">
                                <SearchIcon />
                            </InputAdornment>
                        }
                    />
                </FormControl>
                <table className={classes.table}>
                    <thead className={classes.tableHead}>
                        {[
                            "",
                            "Дата создания",
                            "Пациент",
                            "Сумма",
                            "Комментарий",
                            "Пользователь создавший счет",
                        ].map((item) => (
                            <th key={item}><span>{item}</span></th>
                        ))}
                    </thead>
                    <tbody>
                        {payment.map((item, index) => (
                            <tr key={index}>
                                <td style={{ width: 25 }}></td>
                                <td>{item.register_date}</td>
                                <td>{item.speciality}</td>
                                <td>{item.patient_name}</td>
                                <td>{item.last_visit}</td>
                                <td>{item.payment_date}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <div className={classes.totalAmount}>
                    {/* <TextField
                        label="Сумма"
                        fullWidth
                    /> */}
                </div>
            </div>
        </div>
    );
};

export default RegisteredAccounts;

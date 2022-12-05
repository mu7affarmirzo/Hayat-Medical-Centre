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
import classes from "./registeryVisits.module.scss";
import payment from "../../repositories/data/visits.json";
import BpCheckbox from "../../components/BpCheckbox";

const RegisteryVIsits = () => {
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
                            "Врач",
                            "Специалность",
                            "ФИО клиента",
                            "Дата последного посещения",
                            "Дата услуги",
                            "Дата регистрации",
                            "Цена",
                            "Долг",
                            "Услуги",
                            "Приём состоялся",
                            "Статус",
                            "Скидка",
                            "Отредактирован",
                            "Филиал",
                        ].map((item) => (
                            <th key={item}><span>{item}</span></th>
                        ))}
                    </thead>
                    <tbody>
                        {payment.map((item, index) => (
                            <tr key={index}>
                                <td></td>
                                <td>{item.doctor}</td>
                                <td>{item.speciality}</td>
                                <td>{item.patient_name}</td>
                                <td>{item.last_visit}</td>
                                <td>{item.payment_date}</td>
                                <td>{item.register_date}</td>
                                <td>{item.price}</td>
                                <td>{item.debt}</td>
                                <td><span>{item.service}</span></td>
                                <td className={classes.tableCellMini}>
                                    <BpCheckbox id={index} defaultChecked={false} />
                                </td>
                                <td className={classes.tableCellMini}>{item.status}</td>
                                <td>{item.discount}</td>
                                <td>{item.edited_by}</td>
                                <td>{item.branch}</td>
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

export default RegisteryVIsits;

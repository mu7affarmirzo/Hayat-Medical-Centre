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
import React, { useEffect, useState } from "react";
import { ReactComponent as DownloadAsExcel } from "../../assets/img/excelDownload.svg";
import classes from "./PaymentHistoryView.module.scss";
import payment from "../../repositories/data/closedPayments.json";
import SearchIcon from "@mui/icons-material/Search";
import TransactionsStateKeeper from "../../store/TransactionStateKeeper";
import { useLocalObservable } from "mobx-react-lite";
import { generate_date } from "../../utils/dateFormatter";
import { currencyFormatter } from "../../utils/currencyFormatter";
import { IHistory } from "../../consts/types";
import { DesktopDatePicker } from "@mui/x-date-pickers";
import dayjs, { Dayjs } from "dayjs";

const PaymentHistoryView = () => {
    const transactionStateKeeper = useLocalObservable(() => TransactionsStateKeeper.instance);
    const { gethistory } = transactionStateKeeper
    const [history, setHistory] = useState<IHistory[]>([])
    const [valueFrom, setValueFrom] = React.useState<Dayjs | null>(
        dayjs('2014-08-18T21:11:54'),
    ); const [valueTo, setValueTo] = React.useState<Dayjs | null>(
        dayjs('2014-08-18T21:11:54'),
    );

    const handleChange = (newValue: Dayjs | null) => {
        setValueFrom(newValue);
        console.log(valueFrom?.format('YYYY-MM-DD'))
    };
    const handleChangeTo = (newValue: Dayjs | null) => {
        setValueTo(newValue);
    };
    useEffect(() => {
        gethistory(`?start_date=${valueFrom?.format('YYYY-MM-DD')}&end_date=${valueTo?.format('YYYY-MM-DD')}`).then(res => setHistory(res))
    }, [valueTo])
    return (
        <div className={classes.wrapper}>
            <div className={classes.actions}>
                <div className={classes.formControl}>
                    <FormControl fullWidth>

                        <DesktopDatePicker
                            label="Дата от"
                            inputFormat="YYYY/MM/DD"
                            value={valueFrom}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </FormControl>
                </div>
                <div className={classes.formControl}>
                    <FormControl fullWidth>

                        <DesktopDatePicker
                            label="Дата до"
                            inputFormat="YYYY/MM/DD"
                            value={valueTo}
                            onChange={handleChangeTo}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </FormControl>
                </div>
                <div className={classes.formControl}>
                    <FormControl fullWidth>
                        <InputLabel id="demo-simple-select-label">Операционист</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Операционист"
                        >
                            <MenuItem value={"System system"}>System system</MenuItem>
                            <MenuItem value={"Степан Быков"}>Степан Быков</MenuItem>
                            <MenuItem value={"Василий Новиков"}>Василий Новиков</MenuItem>
                        </Select>
                    </FormControl>
                </div>
                <div className={classes.formControl}>
                    <Button className={classes.downloadButton}>
                        <DownloadAsExcel />
                        <span> Экспорть в Excel</span>
                    </Button>
                </div>
            </div>
            <h3 className={classes.tableTitle}>История закрытий кассы</h3>
            <div className={classes.tableWrapper}>
                <FormControl className={classes.searchbox} variant="standard">
                    <Input
                        placeholder="Введите текст для поиска..."
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
                        {["", "Филиал", "Операционист", "Дата", "Сумма"].map((item) => (
                            <th key={item}>{item}</th>
                        ))}
                    </thead>
                    <tbody>
                        {history.map((item, index) => (
                            <tr key={index}>
                                <td style={{ width: 40 }}></td>
                                <td>{item.branch.name}</td>
                                <td>{item.created_by.f_name}</td>
                                <td>{generate_date(new Date(item.created_at))}</td>
                                <td>{currencyFormatter(item.amount, 'uzs')}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <div className={classes.totalAmount}>
                    <TextField
                        label="Сумма"
                        fullWidth
                        defaultValue={payment
                            .map((i) => i.sum_amount)
                            .reduce((acc, cur) => acc + cur, 0)
                            .toLocaleString(
                                undefined,
                                { minimumFractionDigits: 2 }
                            )}
                    />
                </div>
                <div>
                    <h3 className={classes.tableTitle}>Платежи данного закрытия</h3>
                    <div className={` ${classes.borderTop}`}>

                        <FormControl className={`${classes.searchbox}`} variant="standard">
                            <Input
                                placeholder="Введите текст для поиска..."
                                id="input-with-icon-adornment"
                                endAdornment={
                                    <InputAdornment position="end">
                                        <SearchIcon />
                                    </InputAdornment>
                                }
                            />
                        </FormControl>
                    </div>
                    <table className={classes.table}>
                        <thead className={classes.tableHead}>
                            {["", "Филиал", "Операционист", "Сумма", "Дата"].map((item) => (
                                <th key={item}>{item}</th>
                            ))}
                        </thead>
                        <tbody>
                            {payment.map((item, index) => (
                                <tr key={index}>
                                    <td style={{ width: 40 }}></td>
                                    <td>{item.branch}</td>
                                    <td>{item.operator}</td>
                                    <td>{item.sum_amount}</td>
                                    <td>{item.date}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default PaymentHistoryView;

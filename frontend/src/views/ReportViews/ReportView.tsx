import { Button, FormControlLabel, Switch, TextField } from "@mui/material";
import { Box } from "@mui/system";
import React from "react";
import { ReactComponent as Diagramm } from "../../assets/img/diagramm.svg";
import { ReactComponent as Print } from "../../assets/img/printer.svg";
import { ReactComponent as Excel } from "../../assets/img/excelDownload.svg";
import classes from "./ReportViews.module.scss";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";

const ReportView = () => {
    const [viewType, setViewType] = React.useState<string>("неделя");

    const handleChangeView = (event: React.MouseEvent) => {
        setViewType(event.currentTarget.textContent ?? "");
    };
    return (
        <div className={classes.wrapper}>
            <div className={classes.actions}>
                <Box>
                    <TextField
                        sx={{ marginRight: "10px" }}
                        id="outlined-basic"
                        label="Дата от:"
                        variant="outlined"
                    />
                    <TextField id="outlined-basic" label="Дата до:" variant="outlined" />
                </Box>
                <div
                    className={classes.buttonGroup}
                    aria-label="outlined primary button group"
                >
                    <Button
                        onClick={handleChangeView}
                        variant={viewType === "день" ? "contained" : "outlined"}
                    >
                        день
                    </Button>
                    <Button
                        onClick={handleChangeView}
                        sx={{ borderRadius: 0 }}
                        variant={viewType === "неделя" ? "contained" : "outlined"}
                    >
                        неделя
                    </Button>
                    <Button
                        onClick={handleChangeView}
                        variant={viewType === "месяц" ? "contained" : "outlined"}
                    >
                        месяц
                    </Button>
                </div>
                <TextField
                    sx={{ marginRight: "26px" }}
                    id="outlined-basic"
                    label="Филиал:"
                    variant="outlined"
                />
                <FormControlLabel control={<Switch />} label="Дата платежа" />
                <Button className={`${classes.bordered} ${classes.actionButton}`}>
                    <Diagramm />
                    <span> Диаграмма</span>
                </Button>
                <Button className={classes.actionButton}>
                    <Print />
                    <span>
                        {" "}
                        Печать <br />
                        предпросмотр
                    </span>
                </Button>
                <Button className={classes.actionButton}>
                    <Excel />
                    <span>
                        Экспорть
                        <br />в Excel
                    </span>
                </Button>
            </div>
            <div className={classes.FormControlWrapper}>
                <TextField label="Год" />
                <TextField label="Форма оплаты" />
                <TextField label="Вид платежа" />
                <TextField label="Скидка услуги" />
                <TextField label="Цена услуги" />
                <TextField label="Назначение платежа" />
                <TextField label="Дата услуги" />
                <TextField label="Нал/безнал" />
            </div>
            <table className={classes.tableBody}>
                <thead>
                    <th></th>
                    <th>Услуга</th>
                    <th>Специалность</th>
                    <th>Выберите врача</th>
                    <th>Дата приёма</th>
                    <th>Время начала приёма</th>
                    <th>Время окончания приёма</th>
                </thead>
                <Row />
            </table>
        </div>
    );
};

export default ReportView;

const Row = () => {
    const [open, setOpen] = React.useState(false);

    return (
        <>
            <tr>
                <td></td>
                <td className={classes.alignCenter} onClick={() => setOpen(!open)}>
                    <span
                        className={`${classes.toggler} ${open ? classes.opened : null}`}
                    >
                        {<KeyboardArrowUpIcon />}
                    </span>
                    {"Sardor Akbarov"}
                </td>
                <td>{"Невролог "}</td>
                <td>{"нет данных"}</td>
                <td>{"09.08.2022"}</td>
                <td>{"15:23"}</td>
                <td>{"15:33"}</td>
            </tr>
            <tr style={open ? {} : { display: "none" }}>
                <td></td>
                <td>{""}</td>
                <td>{"Невролог "}</td>
                <td>{"нет данных"}</td>
                <td>{"09.08.2022"}</td>
                <td>{"15:23"}</td>
                <td>{"15:33"}</td>
            </tr>
        </>
    );
};

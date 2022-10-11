import React from 'react';
import {ReactComponent as CalendarEdit} from "../../assets/img/header_icons/calendar-edit.svg";
import styles from "./toolboxs.module.scss";
import parse from 'html-react-parser';
import {Button, Typography} from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";

const Calendar = () => {

    interface ICalendar {
        img: typeof CalendarEdit;
        text: string;
        border?: boolean;
    }

    const calendarData: Array<ICalendar> = [
        {
            img: <CalendarEdit />,
            text: "Создать <br> запись"
        },
        {
            img: <CalendarEdit />,
            text: "Создать <br> событие"
        },
        {
            img: <CalendarEdit />,
            text: "Автозапись"
        },
        {
            img: <CalendarEdit />,
            text: "Найти <br> время"
        },
        {
            img: <CalendarEdit />,
            text: "Выдать <br> счет"
        },
        {
            img: <CalendarEdit />,
            text: "Печать",
            border: true
        },
        {
            img: <CalendarEdit />,
            text: "Отмененные"
        },
    ]

    return (
        <div className={styles.calendar}>
            <div className={styles.left_side}>
                <div className={styles.tools}>
                    {calendarData.map(item => (
                        <div className={`${styles.tools_item} ${item.border ? styles.border : ""}`}>
                            {item.img}
                            <span>{parse(item.text)}</span>
                        </div>
                    ))}
                </div>
                <div className={styles.calendar_block}>
                    <div className={styles.calendar_wrapper}>
                        <div className={styles.left}>
                            <p className={styles.name}>Интервал</p>
                            <p className={styles.days}>20.06.2022 - 05.08.2022</p>
                        </div>

                        <ArrowDropDownIcon sx={{fill: "rgba(0, 0, 0, 0.54)"}} />
                    </div>
                </div>
            </div>

            <Button variant="contained" className={styles.create_btn} startIcon={<CalendarEdit />}>
                Создать запись
            </Button>
        </div>
    );
};

export default Calendar;
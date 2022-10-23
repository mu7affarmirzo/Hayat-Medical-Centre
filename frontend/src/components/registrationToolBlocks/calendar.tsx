import React from 'react';
import {ReactComponent as CalendarEdit} from "../../assets/img/header_icons/calendar-edit.svg";
import {ReactComponent as NoteAdd} from "../../assets/img/note-add.svg";
import {ReactComponent as CalendarAdd} from "../../assets/img/calendar-add.svg";
import {ReactComponent as DocumentForward} from "../../assets/img/document-forward.svg";
import {ReactComponent as CalendarSearch} from "../../assets/img/calendar-search.svg";
import {ReactComponent as ReceiptItem} from "../../assets/img/receipt-item.svg";
import {ReactComponent as Printer} from "../../assets/img/printer.svg";
import {ReactComponent as CalendarRemove} from "../../assets/img/calendar-remove.svg";
import styles from "./toolboxs.module.scss";
import parse from 'html-react-parser';
import {Button} from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import {Link} from "react-router-dom";

const Calendar = () => {

    interface ICalendar {
        img: typeof CalendarEdit;
        text: string;
        border?: boolean;
    }

    const calendarData: Array<ICalendar> = [
        {
            img: <NoteAdd />,
            text: "Создать <br> запись"
        },
        {
            img: <CalendarAdd />,
            text: "Создать <br> событие"
        },
        {
            img: <DocumentForward />,
            text: "Автозапись"
        },
        {
            img: <CalendarSearch />,
            text: "Найти <br> время"
        },
        {
            img: <ReceiptItem />,
            text: "Выдать <br> счет"
        },
        {
            img: <Printer />,
            text: "Печать",
            border: true
        },
        {
            img: <CalendarRemove />,
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

            <Link to="/createNote">
                <Button variant="contained" className={styles.create_btn} startIcon={<CalendarEdit />}>
                    Создать запись
                </Button>
            </Link>
        </div>
    );
};

export default Calendar;
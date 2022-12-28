import React from 'react';
import { ReactComponent as CalendarEdit } from "../../assets/img/header_icons/calendar-edit.svg";
import { ReactComponent as NoteAdd } from "../../assets/img/note-add.svg";
import { ReactComponent as CalendarAdd } from "../../assets/img/calendar-add.svg";
import { ReactComponent as DocumentForward } from "../../assets/img/document-forward.svg";
import { ReactComponent as CalendarSearch } from "../../assets/img/calendar-search.svg";
import { ReactComponent as ReceiptItem } from "../../assets/img/receipt-item.svg";
import { ReactComponent as Printer } from "../../assets/img/printer.svg";
import { ReactComponent as CalendarRemove } from "../../assets/img/calendar-remove.svg";
import styles from "./toolboxs.module.scss";
import parse from 'html-react-parser';
import { Box, Button, FormControl, InputLabel, MenuItem, Select, SelectChangeEvent } from "@mui/material";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import { Link } from "react-router-dom";
import Modal from '../Modal';
import CreateDoctorEvent from '../CreateDoctorEvent';



const Calendar = () => {

    const [createEventModal, setCreateEventModal] = React.useState(false);

    interface ICalendar {
        img: typeof CalendarEdit;
        text: string;
        border?: boolean;
        type: string
    }

    const calendarData: Array<ICalendar> = [
        {
            img: <NoteAdd />,
            text: "Создать <br> запись",
            type: ''
        },
        // {
        //     img: <CalendarAdd />,
        //     text: "Создать <br> событие",
        //     type: 'create_event'
        // },
        // {
        //     img: <DocumentForward />,
        //     text: "Автозапись",
        //     type: ''
        // },
        // {
        //     img: <CalendarSearch />,
        //     text: "Найти <br> время",
        //     type: ''
        // },
        {
            img: <ReceiptItem />,
            text: "Выдать <br> счет",
            type: ''
        },
        {
            img: <Printer />,
            text: "Печать",
            border: true,
            type: ''
        },
        // {
        //     img: <CalendarRemove />,
        //     text: "Отмененные",
        //     type: ''
        // },
    ]

    const navbarClickHandler = (event) => {
        if (event.target.dataset.type === 'create_event') {
            setCreateEventModal(true)
        }
    }

    const [interval, setInterVal] = React.useState('');


    return (
        <div className={styles.calendar}>
            {createEventModal ? (
                <Modal
                    show={createEventModal}
                    onClose={() => setCreateEventModal(false)}
                >
                    <CreateDoctorEvent />
                </Modal>
            ) : null}
            <div className={styles.left_side}>
                <div className={styles.tools}>
                    {calendarData.map((item, index) => (
                        <div key={index} data-type={item.type} onClick={navbarClickHandler} className={`${styles.tools_item} ${item.border ? styles.border : ""}`}>
                            {item.img}
                            <span>{parse(item.text)}</span>
                        </div>
                    ))}
                </div>
                <div className={styles.calendar_block}>
                    <Box sx={{ minWidth: 120 }}>
                        <FormControl fullWidth >
                            <InputLabel id="demo-simple-select-label">Интервал</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                defaultValue={'10'}
                                value={interval}
                                label="Интервал"
                                onChange={(event: SelectChangeEvent) => setInterVal(event.target.value as string)}
                            >
                                <MenuItem value={10}>10 мин</MenuItem>
                                <MenuItem value={20}>20 мин</MenuItem>
                                <MenuItem value={30}>30 мин</MenuItem>
                            </Select>
                        </FormControl>
                    </Box>
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
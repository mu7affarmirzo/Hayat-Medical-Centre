import React, {useState} from 'react';
import styles from "./index.module.scss";
import ToolBoxTop from "../../components/registrationToolBlocks/main";
import {Alert, Box, FormControl, Grid, InputLabel, MenuItem, OutlinedInput, Select, Snackbar} from "@mui/material";
import {ReactComponent as SearchNormal} from "../../assets/img/search-normal.svg"
import "react-big-calendar/lib/css/react-big-calendar.css";
import CalendarMain from "../../components/calendar/main";
import { IBranch, IDoctor, ISpeciality } from "../../consts/types";
import {observer, useLocalObservable} from "mobx-react-lite";
import moment from "moment";
import {CalendarEventStateKeeper} from "../../store";
import ErrorNotification from "../../store/ErrorNotification";


const MainView = observer((
    {
        selectData,
        setSelectData,
        specialities,
        doctors,
        changeSpecialty,
        onSelectDoctor,
        selectedDoctors,
        searchInputsValue,
        searchInputsHandler,
        branchesCopy,
        handleChangeBranch
    }: {
        selectData: string
        setSelectData: (str: string) => void
        specialities: Array<ISpeciality>
        doctors: Array<IDoctor>
        changeSpecialty: (id: string) => void
        onSelectDoctor: (e: React.MouseEvent<HTMLElement> | React.ChangeEvent<HTMLInputElement>, data: IDoctor) => void
        selectedDoctors: Array<IDoctor>
        searchInputsValue: {specialities: string, doctors: string}
            searchInputsHandler: (type: string, value: string) => void,
            branchesCopy: Array<IBranch>,
            handleChangeBranch: (str: string) => void
    }
) => {
    const {openNotification, changeVisibilityNotification} = useLocalObservable(() => ErrorNotification.instance);

    React.useEffect(() => {

    }, [])

    const changeButtons: Array<{ text: string, type: string }> = [
        {
            text: "месяц",
            type: "month"
        },
        {
            text: "неделя",
            type: "week"
        },
        {
            text: "день",
            type: "day"
        },

    ];
    const calendarEventsStateKeeper = useLocalObservable(() => CalendarEventStateKeeper.instance);
    const {changeViewFunctions} = calendarEventsStateKeeper;

    const [active, setActive] = useState<string>("month");

    const changeView = (type: string) => {
        setActive(type);
        console.log(type, "changeView")
        changeViewFunctions.forEach(item => item(type))
    }

    const convertDate = () => {
        const momentRu = moment().locale("ru")
        if (active === "month") {
            return momentRu.format("MMMM YYYY")
        } else if (active === "week") {
            let startWeek = momentRu.startOf("week").format("DD MMMM YYYY");
            let endWeek = momentRu.endOf("week").format("DD MMMM YYYY");
            return `${startWeek} - ${endWeek}`;
        } else if (active === "day") {
            return momentRu.format("dddd | DD MMMM");
        }
    }
    return (
        <>
            <div className={styles.main_block}>
                <div className={styles.top}>
                    <ToolBoxTop/>
                </div>

                <div className={styles.main_content}>
                    <div className={styles.table}>
                        <Box sx={{mb: "10px"}}>
                            <FormControl fullWidth>
                                <InputLabel id="demo-simple-select-label">Филиал</InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    value={selectData}
                                    label="Филиал"
                                    onChange={(e) => handleChangeBranch(e.target.value)}
                                >
                                    {
                                        branchesCopy.map((item, index) => (
                                            <MenuItem key={index} value={item.id}>{item.name}</MenuItem>
                                        ))
                                    }
                                </Select>
                            </FormControl>
                        </Box>


                        <Grid container mb="10px">
                            <Grid item xl={6}>
                                <FormControl sx={{width: "301px", height: "100%", marginRight: "20px"}}
                                             variant="outlined">
                                    <InputLabel htmlFor="outlined-adornment-password">Поиск специалности</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-password"
                                        type={'text'}
                                        value={searchInputsValue.specialities}
                                        onChange={(e) => searchInputsHandler("specialities", e.target.value)}
                                        endAdornment={
                                            <SearchNormal position="end"/>
                                        }
                                        label="Поиск специалности"
                                    />
                                </FormControl>
                            </Grid>
                            <Grid item xl={6} sx={{textAlign: "right"}}>
                                <FormControl sx={{width: "301px", height: "100%"}} variant="outlined">
                                    <InputLabel htmlFor="outlined-adornment-password">Поиск врачей</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-password"
                                        type={'text'}
                                        value={searchInputsValue.doctors}
                                        onChange={(e) => searchInputsHandler("doctors", e.target.value)}
                                        endAdornment={
                                            <SearchNormal position="end"/>
                                        }
                                        label="Поиск врачей"
                                    />
                                </FormControl>
                            </Grid>
                        </Grid>


                        <div className={styles.table_block}>
                            <div className={`${styles.table_medical} ${styles.custom_scrollbar}`}>
                                <div onClick={() => changeSpecialty("all")} className={styles.table_item}>Все</div>
                                {
                                    specialities.map((item, i) => (
                                        <div
                                            onClick={() => changeSpecialty(item.id)}
                                            // style={{ backgroundColor: item.color }}
                                            className={styles.table_item}
                                            key={item.id}
                                        >
                                            {item.name}
                                        </div>
                                    ))
                                }
                            </div>

                            <div className={`${styles.table_doctors} ${styles.custom_scrollbar}`}>
                                {
                                    doctors.map((item: IDoctor) => (
                                        <div
                                            onClick={(e) => onSelectDoctor(e, item)}
                                            key={item.id}
                                            className={`doctors_table_row ${styles.row} ${selectedDoctors.map((doctor) => doctor.id).includes(item.id) ? styles.selected : ""}`}
                                            // style={{backgroundColor: item.color}}
                                        >
                                            <div className={styles.cell}>
                                                <label className={styles.checkbox_block}>
                                                    <input
                                                        type="checkbox"
                                                        checked={selectedDoctors.map((doctor) => doctor.id).includes(item.id)}
                                                        onChange={(e) => onSelectDoctor(e, item)}
                                                    />
                                                    <div className={styles.box}></div>
                                                </label>
                                            </div>
                                            <div className={styles.cell}>
                                                {item?.email}
                                            </div>
                                            <div className={styles.cell}>
                                                {/* {item.speciality.name} */}
                                            </div>
                                            <div className={styles.cell}>
                                                {item.phone_number}
                                            </div>
                                            <div className={styles.cell}>
                                                <div
                                                    className={`${styles.status_block} ${item.active ? "" : styles.not_active}`}></div>
                                            </div>
                                        </div>
                                    ))
                                }

                            </div>
                        </div>
                    </div>
                    <div className={styles.calendar}>
                        {
                            selectedDoctors.length > 0 &&

                            <div className={styles.toolbar}>
                                <div className={styles.button_now}>Сегодня</div>
                                <p className={styles.now_day}> {convertDate()}</p>

                                <div className={`month_buttons_block ${styles.buttons_change}`}>
                                    {changeButtons.map((item, i) => (
                                        <div
                                            key={item.type}
                                            onClick={(e) => changeView(item.type)}
                                            className={`month_buttons ${styles.button_item} ${item.type === active ? `month_button_active ${styles.active}` : ""}`}
                                            data-type={item.type}
                                        >
                                            {item.text}
                                        </div>
                                    ))}
                                </div>
                            </div>
                        }
                        <div className={styles.calendar_main}>
                            <CalendarMain/>
                        </div>
                    </div>
                </div>
            </div>

            <Snackbar
                open={openNotification}
                autoHideDuration={3000}
                onClose={() => changeVisibilityNotification(false)}
                anchorOrigin={{ vertical: "top", horizontal: "right" }}
            >
                <Alert
                    onClose={() => changeVisibilityNotification(false)}
                    severity="error"
                    sx={{ width: '100%' }}
                >
                    Пожалуйста выберете сначала доктора
                </Alert>
            </Snackbar>
        </>
    );
});

export default MainView;
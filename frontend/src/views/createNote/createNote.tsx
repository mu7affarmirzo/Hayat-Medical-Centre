import React, {useState} from 'react';
import {FlexSpaceBetween} from "../../themes/customItems";
import {Link} from "react-router-dom";
import {Backdrop, Box, Button, TextField, Typography} from "@mui/material";
import styles from "./index.module.scss"
import {ReactComponent as NoteAdd} from "../../assets/img/note-add.svg";
import {ReactComponent as CloseCircle} from "../../assets/img/close-circle.svg";
import {ReactComponent as UserAdd} from "../../assets/img/user-add.svg";
import Edit from "../../assets/img/edit.svg";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowCircle from "../../assets/img/arrow-circle-left.svg"
import moment from "moment"
import PatientsTable from "./patientsTable";

const CreateNote = () => {
    interface IDateValue {
        from: moment.Moment | null
        to: moment.Moment | null
    }

    const [openPatientsPopup, setOpenPatients] = useState<boolean | string>(false);
    const [selectData, setSelectData] = useState<string>("");
    const [timeValue, setTimeValue] = React.useState<IDateValue>({
        from: moment(),
        to: moment().add(5, 'minutes')
    });

    const [dateValue, setDateValue] = React.useState<moment.Moment | null>(moment());

    const timeChangeHandler = (time, type) => {
        setTimeValue({...timeValue, [type]: time})
    }

    return (
        <div className={styles.create_note}>
            <FlexSpaceBetween className={styles.top_block}>
                <Link to="/test" className={styles.return_back}>
                    <img src={ArrowCircle} alt="ArrowCircle"/>
                    <p>Запись на прием - ЛОР</p>
                </Link>

                <div className={styles.buttons}>
                    <Button sx={{backgroundColor: "#64B6F7"}} variant="contained" className={styles.create_btn} startIcon={<NoteAdd />}>
                        Создать
                    </Button>
                    <Link to="/test">
                        <Button sx={{backgroundColor: "#BDBDBD", marginLeft: "10px"}} variant="contained" className={styles.create_btn} startIcon={<CloseCircle />}>
                            Отмена
                        </Button>
                    </Link>
                </div>
            </FlexSpaceBetween>

            <FlexSpaceBetween mt="17px">
                <Box className={styles.choose_block} onClick={() => setOpenPatients(true)} >
                    <p className={styles.title}>Выберите пациента</p>
                    <FlexSpaceBetween>
                        <p className={styles.text}>ФИО пациента</p>
                        <ArrowDropDownIcon />
                    </FlexSpaceBetween>
                </Box>

                <Backdrop
                    open={Boolean(openPatientsPopup)}
                    onClick={(e: any) => {

                        if(!e.target.closest(`.${styles.patients_popup}`))
                            setOpenPatients(false);
                    }}
                    sx={{zIndex: "999"}}
                >
                    <Box className={styles.patients_popup}>
                        <Typography variant="h5" className={styles.title}>Пациенты</Typography>

                        <div className={styles.patients_wrapper}>
                            <TextField id="outlined-basic" label="ФИО пациента" variant="outlined" className={styles.patients_item}/>
                            <TextField id="outlined-basic" label="ИНН" variant="outlined" className={styles.patients_item}/>
                            <TextField id="outlined-basic" label="№ мед карты" variant="outlined" className={styles.patients_item}/>
                            <TextField id="outlined-basic" label="Дата рождения" variant="outlined" className={styles.patients_item}/>
                            <TextField id="outlined-basic" label="Телефон" variant="outlined" className={styles.patients_item}/>
                            <TextField id="outlined-basic" label="ID пациента" variant="outlined" className={styles.patients_item}/>
                            <TextField id="outlined-basic" label="Дата приёма" variant="outlined" className={styles.patients_item}/>
                            <Button
                                variant="contained"
                                className={styles.create_btn}
                                startIcon={<UserAdd className="svg_stroke_white" />}
                                sx={{backgroundColor: "#64B6F7", height: "56px", width: "244px", marginBottom: "10px"}}
                            >
                                Добавить Пациента
                            </Button>
                        </div>

                        <div className={styles.table_block}>
                            <div className={styles.table_top}>
                                <div className={styles.top_title}>Фамилия</div>
                                <div className={styles.top_title}>Имя</div>
                                <div className={styles.top_title}>Отчества</div>
                                <div className={styles.top_title}>Дата рождения</div>
                                <div className={styles.top_title}>Мобильный телефон</div>
                                <div className={styles.top_title}>ID номер</div>
                                <div className={styles.top_title}>Дата последнего посещения</div>
                                <div className={styles.top_title}></div>
                            </div>

                            <div className={styles.table}>
                                <table>
                                    <tbody>
                                    <tr>
                                        <td>Лебедев</td>
                                        <td>Сергей </td>
                                        <td>Васильевич</td>
                                        <td>25.07.2022</td>
                                        <td>(834) 295-1534</td>
                                        <td></td>
                                        <td>25.07.2022 14:10</td>
                                        <td>
                                            <img src={Edit} alt="edit"/>
                                        </td>
                                    </tr>

                                    <tr>
                                        <td>Лебедев</td>
                                        <td>Сергей </td>
                                        <td>Васильевич</td>
                                        <td>25.07.2022</td>
                                        <td>(834) 295-1534</td>
                                        <td></td>
                                        <td>25.07.2022 14:10</td>
                                        <td>
                                            <img src={Edit} alt="edit"/>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>


                        <div className={styles.patients_bottom}>
                            <div className={`${styles.btn} ${styles.show}`}>Показать</div>
                            <div className={`${styles.btn} ${styles.cancel}`} onClick={() => setOpenPatients(false)}>Отмена</div>
                        </div>
                    </Box>
                </Backdrop>

                <Button
                    sx={{backgroundColor: "#007DFF", height: "42px"}}
                    variant="contained"
                    className={styles.create_btn}
                    startIcon={<UserAdd className="svg_stroke_white" />}
                >
                    Добавить Пациента
                </Button>
            </FlexSpaceBetween>


            <PatientsTable
                selectData={selectData}
                setSelectData={setSelectData}
                timeValue={timeValue}
                dateValue={dateValue}
                setDateValue={setDateValue}
                timeChangeHandler={timeChangeHandler}
            />
        </div>
    );
};

export default CreateNote;
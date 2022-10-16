import React, {useState} from 'react';
import {FlexSpaceBetween} from "../../themes/customItems";
import {Link} from "react-router-dom";
import {
    Backdrop,
    Box,
    Button, Checkbox,
    Drawer,
    FormControl, FormControlLabel,
    InputLabel,
    MenuItem,
    Select,
    TextField,
    Typography
} from "@mui/material";
import styles from "./index.module.scss"
import {ReactComponent as NoteAdd} from "../../assets/img/note-add.svg";
import {ReactComponent as CloseCircle} from "../../assets/img/close-circle.svg";
import {ReactComponent as UserAdd} from "../../assets/img/user-add.svg";
import Edit from "../../assets/img/edit.svg";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import ArrowCircle from "../../assets/img/arrow-circle-left.svg"

const CreateNote = () => {
    const [openPatientsPopup, setOpenPatients] = useState<boolean | string>(false);
    const [selectData, setSelectData] = useState<string>("");

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


            <div className={styles.patients_main_table}>
                <div className={styles.left_table}>
                    <div className={styles.table_title}>Детали</div>
                    <div className={styles.table_wrapper}>
                        <div className={styles.table_row} style={{paddingBottom: "10px", borderBottom: "1px solid #E0E0E0"}}>
                            <p className={styles.row_title} style={{marginRight: "30px"}}>Льгота</p>

                            <FormControl className={styles.table_dropdown} >
                                <InputLabel id="demo-simple-select-label" sx={{top: "-12px"}}>Без скидок</InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    value={selectData}
                                    label="Филиал"
                                    onChange={(e) => setSelectData(e.target.value)}
                                    sx={{height: "32px"}}
                                >
                                    <MenuItem value={"head1"}>Головной1</MenuItem>
                                    <MenuItem value={"head2"}>Головной2</MenuItem>
                                    <MenuItem value={"head3"}>Головной3</MenuItem>
                                </Select>
                            </FormControl>
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title} style={{marginRight: "17px"}}>Дата приема</p>

                            <div style={{width: "275px", height: "32px", marginRight: "17px"}}></div>

                            <FormControlLabel control={<Checkbox />} label="Авто" sx={{marginRight: "10px"}}/>
                        </div>

                        <div className={styles.table_row}>
                            <p className={styles.row_title} style={{marginRight: "17px"}}>Время начала</p>

                            <div style={{width: "275px", height: "32px", marginRight: "17px"}}></div>

                            <FormControlLabel control={<Checkbox />} label="Авто" />
                        </div>
                    </div>
                </div>
                <div className={styles.right_table}></div>
            </div>
        </div>
    );
};

export default CreateNote;
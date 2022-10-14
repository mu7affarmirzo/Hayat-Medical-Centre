import React from 'react';
import Headers from "../../components/headers";
import styles from "./index.module.scss";
import SideBar from "../../components/sideBar";
import ToolBoxTop from "../../components/registrationToolBlocks/main";
import {Box, FormControl, Grid, InputLabel, MenuItem, OutlinedInput, Select} from "@mui/material";
import {ReactComponent as SearchNormal} from "../../assets/img/search-normal.svg"

import "react-big-calendar/lib/css/react-big-calendar.css";
// import 'react-big-calendar/lib/sass/styles';
import CalendarMain from "../../components/calendar/main";


const MainIndex = () => {
    const [selectData, setSelectData] = React.useState('');


    return (
        <div>
            <Headers/>
            <div className={styles.main_wrapper}>
                <SideBar/>
                <div className={styles.main_block}>
                    <div className={styles.top}>
                        <ToolBoxTop/>
                    </div>

                    <div className={styles.main_content}>
                        <div className={styles.table}>
                            <Box sx={{mb: "10px"}}>
                                <FormControl fullWidth>
                                    <InputLabel id="demo-simple-select-label">Age</InputLabel>
                                    <Select
                                        labelId="demo-simple-select-label"
                                        id="demo-simple-select"
                                        value={selectData}
                                        label="Филиал"
                                        onChange={(e) => setSelectData(e.target.value)}
                                    >
                                        <MenuItem value={"head1"}>Головной1</MenuItem>
                                        <MenuItem value={"head2"}>Головной2</MenuItem>
                                        <MenuItem value={"head3"}>Головной3</MenuItem>
                                    </Select>
                                </FormControl>
                            </Box>


                            <Grid container mb="10px">
                                <Grid item xl={6}>
                                    <FormControl sx={{width: "301px", height: "100%", marginRight: "20px"}}
                                                 variant="outlined">
                                        <InputLabel htmlFor="outlined-adornment-password">Поиск
                                            специалности</InputLabel>
                                        <OutlinedInput
                                            id="outlined-adornment-password"
                                            type={'text'}
                                            // value={values.password}
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
                                            // value={values.password}
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
                                    <div className={styles.table_item}>Все</div>
                                    <div className={styles.table_item}>Акушер-гинекоasdasd</div>
                                    <div className={styles.table_item}>Андролог</div>
                                </div>

                                <div className={`${styles.table_doctors} ${styles.custom_scrollbar}`}>
                                    <div className={styles.row}>
                                        <div className={styles.cell}>
                                            <label className={styles.checkbox_block}>
                                                <input type="checkbox"/>
                                                <div className={styles.box}></div>
                                            </label>
                                        </div>
                                        <div className={styles.cell}>
                                            Михаил Романов
                                        </div>
                                        <div className={styles.cell}>
                                            Педиатр
                                        </div>
                                        <div className={styles.cell}>
                                            (210) 727-9289
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles.calendar}>
                            <CalendarMain/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MainIndex;
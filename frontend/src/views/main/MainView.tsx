import React from 'react';
import styles from "./index.module.scss";
import ToolBoxTop from "../../components/registrationToolBlocks/main";
import {Box, FormControl, Grid, InputLabel, MenuItem, OutlinedInput, Select} from "@mui/material";
import {ReactComponent as SearchNormal} from "../../assets/img/search-normal.svg"
import "react-big-calendar/lib/css/react-big-calendar.css";
import CalendarMain from "../../components/calendar/main";
import {IDoctor, ISpeciality} from "../../consts/types";
import {observer} from "mobx-react-lite";


const MainView = observer((
    {
        selectData,
        setSelectData,
        specialities,
        doctors,
        changeSpecialty,
        onSelectDoctor,
        selectedDoctor,
    }: {
        selectData: string
        setSelectData: (str: string) => void
        specialities: Array<ISpeciality>
        doctors: Array<IDoctor>
        changeSpecialty: (id: string) => void
        onSelectDoctor: (e: React.MouseEvent<HTMLElement> | React.ChangeEvent<HTMLInputElement>, data: IDoctor) => void
        selectedDoctor: Array<string>
    }
) => {
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
                                    <InputLabel htmlFor="outlined-adornment-password">Поиск специалности</InputLabel>
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
                                    specialities.map(item => (
                                        <div
                                            onClick={() => changeSpecialty(item.id)}
                                            // style={{backgroundColor: item.color}}
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
                                            className={`doctors_table_row ${styles.row} ${selectedDoctor.includes(item.id) ? styles.selected : ""}`}
                                            // style={{backgroundColor: item.color}}
                                        >
                                            <div className={styles.cell}>
                                                <label className={styles.checkbox_block}>
                                                    <input
                                                        type="checkbox"
                                                        checked={selectedDoctor.includes(item.id)}
                                                        onChange={(e) => onSelectDoctor(e, item)}
                                                    />
                                                    <div className={styles.box}></div>
                                                </label>
                                            </div>
                                            <div className={styles.cell}>
                                                {item.full_name}
                                            </div>
                                            <div className={styles.cell}>
                                                {item.speciality.name}
                                            </div>
                                            <div className={styles.cell}>
                                                {item.number}
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
                        <CalendarMain/>
                    </div>
                </div>
            </div>
        </>
    );
});

export default MainView;
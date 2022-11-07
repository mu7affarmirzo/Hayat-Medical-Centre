import {
    Button,
    FormControl,
    InputLabel,
    MenuItem,
    Select,
    TextField,
} from "@mui/material";
import React from "react";
import classes from "./createDoctorEvent.module.scss";
import Grid from "@mui/material/Unstable_Grid2";
import { DesktopDatePicker, TimePicker } from "@mui/x-date-pickers";
import dayjs, { Dayjs } from "dayjs";

const CreateDoctorEvent = () => {
    const [value, setValue] = React.useState<Dayjs | null>(
        dayjs("2014-08-18T21:11:54")
    );

    const handleChange = (newValue: Dayjs | null) => {
        setValue(newValue);
    };

    return (
        <div className={classes.card}>
            <h6 className={classes.title}>Событие врача</h6>
            <Grid container spacing={2}>
                <Grid md={12}>
                    <FormControl fullWidth className={classes.formControl}>
                        <InputLabel id="demo-simple-select-label">Событие</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Событие"
                        >
                            <MenuItem value={"Обеденный перерыв"}>Обеденный перерыв</MenuItem>
                            <MenuItem value={20}>Twenty</MenuItem>
                            <MenuItem value={30}>Thirty</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid md={4}>
                    <FormControl fullWidth>
                        <DesktopDatePicker
                            label="Дата начало"
                            inputFormat="MM/DD/YYYY"
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </FormControl>
                </Grid>
                <Grid md={4}>
                    <FormControl fullWidth>
                        <TimePicker
                            label="Время начало"
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </FormControl>
                </Grid>
                <Grid md={4}>
                    <FormControl fullWidth>
                        <TimePicker
                            label="Время завершения"
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </FormControl>
                </Grid>
                <Grid md={12}>
                    <FormControl fullWidth>
                        <TextField
                            id="outlined-multiline-static"
                            label="Заметки"
                            multiline
                            rows={6}
                        />
                    </FormControl>
                </Grid>
                <Grid md={3}>
                    <Button fullWidth variant="outlined">ОК</Button>
                </Grid>
                <Grid md={3}>
                    <Button fullWidth variant="outlined" >Удалить</Button>
                </Grid>
                <Grid md={3}>
                    <Button fullWidth variant="outlined" >Отмена</Button>
                </Grid>
                <Grid md={3}>
                    <Button fullWidth variant="outlined" >Повтор</Button>
                </Grid>
            </Grid>
        </div >
    );
};

export default CreateDoctorEvent;

import { FormControl, FormControlLabel, FormGroup, Switch, TextField } from "@mui/material";
import React from "react";
import classes from "./SearchPanel.module.scss";

const SearchPanel = () => {
    return (
        <FormGroup className={classes.wrapper}>
            <FormControl className={classes.inputHolder}>
                <TextField name="name" id="outlined-basic" label="ФИО" variant="outlined" />
            </FormControl>
            <FormControl className={classes.inputHolder}>
                <TextField
                    id="outlined-basic" name="phone"
                    label="Моб. телефон"
                    variant="outlined"
                />
            </FormControl>
            <FormControl className={classes.inputHolder}>
                <TextField
                    id="outlined-basic" name="birthdate"
                    label="Дата рождения"
                    variant="outlined"
                />
            </FormControl>
            <FormControl className={classes.inputHolder}>
                <TextField name="id" id="outlined-basic" label="ID номер" variant="outlined" />
            </FormControl>
            <FormControl className={classes.inputHolder}>
                <TextField id="outlined-basic" name="email" label="Эл. почта" variant="outlined" />
            </FormControl>
            <FormControl className={classes.inputHolder}>
                <TextField id="outlined-basic" name="register_date" label="Дата регистрации" variant="outlined" />
            </FormControl>
            <FormControlLabel control={<Switch defaultChecked />} label="Только активные" />
        </FormGroup>
    );
};

export default SearchPanel;

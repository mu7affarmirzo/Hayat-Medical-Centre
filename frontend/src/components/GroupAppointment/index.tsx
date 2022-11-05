import React from 'react';
import Grid from "@mui/material/Unstable_Grid2";

import classes from './GroupAppointment.module.scss';
import { Button, FormControl, MenuItem, Paper, Select, TextField } from '@mui/material';
import { ReactComponent as SearchIcon } from '../../assets/img/header_icons/search-normal.svg';

const GroupAppointment = () => {
    return (
        <div className={classes.group}>
            <h2 className={classes.title}>Добавить новой записи</h2>
            <Grid container spacing={10} >
                <Grid md={8}>
                    <FormControl fullWidth className={classes.formControl}>
                        <TextField
                            name='id'
                            // onChange={handleTextFieldChange}
                            label="Выберите клиента "
                            type="text"
                        />
                    </FormControl>
                    <FormControl style={{ marginBottom: 10 }} fullWidth className={classes.formControl}>
                        <Select label='Выберите пакет' labelId="demo-simple-select-label" id="demo-simple-select">
                            <MenuItem value={'Не выбрана'}>Не выбрана</MenuItem>
                            <MenuItem value={10}>Ten</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid md={4}>
                    <FormControl fullWidth className={classes.formControl}>
                        <TextField
                            name='id'
                            // onChange={handleTextFieldChange}
                            label="Стоимость пакета "
                            type="text"
                        />
                    </FormControl>
                    <Button size='large' color='primary' variant='contained' fullWidth>
                        Авто расстановка
                    </Button>
                </Grid>
            </Grid>
            <Grid container spacing={10}>
                <Grid md={12}>
                    <div className={classes.table}>
                        <div className={classes.tableHeader}>
                            <SearchIcon />
                            <TextField style={{ all: 'unset', width: '100%' }} type={'search'} placeholder='Поиск по таблице' fullWidth />
                        </div>
                    </div>
                </Grid>
            </Grid>
        </div>
    )
}

export default GroupAppointment
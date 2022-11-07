import React from 'react';
import Grid from "@mui/material/Unstable_Grid2";
import { ReactComponent as CalendarEdit } from "../../assets/img/note-add.svg";
import { ReactComponent as SearchIcon } from '../../assets/img/header_icons/search-normal.svg';
import { ReactComponent as EditIcon } from '../../assets/img/edit.svg';
import { Button, FormControl, InputLabel, MenuItem, Select, TextField } from '@mui/material';

import classes from './GroupAppointment.module.scss';

const GroupAppointment = () => {
    return (
        <div className={classes.group}>
            <h2 className={classes.title}>Добавить новой записи</h2>
            <Grid container spacing={10} >
                <Grid md={8}>
                    <div className={classes.row}>
                        <FormControl fullWidth className={classes.formControl}>
                            <InputLabel id="demo-simple-select-label">Выберите клиента</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                label="Выберите клиента"
                            >
                                <MenuItem value={'Лебедев Сергей Васильевич'}>Лебедев Сергей Васильевич</MenuItem>
                                <MenuItem value={20}>Twenty</MenuItem>
                                <MenuItem value={30}>Thirty</MenuItem>
                            </Select>
                        </FormControl>
                        <Button variant='outlined'>
                            <CalendarEdit />
                        </Button>
                        <Button variant='outlined'>
                            <EditIcon />
                        </Button>
                    </div>
                    <FormControl style={{ marginBottom: 10 }} fullWidth className={classes.formControl}>
                        <InputLabel id="demo-simple-select-label">Выберите пакет</InputLabel>
                        <Select label='Выберите пакет' labelId="demo-simple-select-label" id="demo-simple-select">
                            <MenuItem value={'Не выбрана'}>Не выбрана</MenuItem>
                            <MenuItem value={10}>Ten</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid md={4}>
                    <FormControl fullWidth className={classes.formControl}>
                        <InputLabel id="demo-simple-select-label">Age</InputLabel>
                        <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            label="Age"
                        >
                            <MenuItem value={10}>Ten</MenuItem>
                            <MenuItem value={20}>Twenty</MenuItem>
                            <MenuItem value={30}>Thirty</MenuItem>
                        </Select>
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
                        <table className={classes.tableBody}>
                            <thead>
                                <th></th>
                                <th>Услуга</th>
                                <th>Специалность</th>
                                <th>Выберите врача</th>
                                <th>Дата приёма</th>
                                <th>Время начала приёма</th>
                                <th>Время окончания приёма</th>
                            </thead>
                            <tr>
                                <td></td>
                                <td >{'Однозначно, стремящиеся вытеснить традиционное производство, нанотехнологии представляют собой не что иное, как квинтэссенцию победы маркетинга над разумом и должны быть описаны максимально подробно.'}</td>
                                <td>{'Невролог '}</td>
                                <td>{'нет данных'}</td>
                                <td>{'09.08.2022'}</td>
                                <td>{'15:23'}</td>
                                <td>{'15:33'}</td>
                            </tr>
                        </table>
                    </div>
                </Grid>
            </Grid>
        </div>
    )
}

export default GroupAppointment
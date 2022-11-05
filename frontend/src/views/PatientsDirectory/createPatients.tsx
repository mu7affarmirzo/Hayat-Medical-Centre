import * as React from "react";
import Grid from "@mui/material/Unstable_Grid2";
import classes from "./createPatient.module.scss";
import { Button, Checkbox, FormControl, FormControlLabel, FormLabel, Radio, RadioGroup, TextField } from "@mui/material";
import Tabber from "./tabber";
import { PatientsDirectoryEditActions } from "../../consts/patientsDirectory";
import { ReactComponent as ArrowCircleLeft } from '../../assets/img/arrow-circle-left.svg'
import { Link, useNavigate } from "react-router-dom";

const CreatePatients = () => {
    const [state, setState] = React.useState<object[]>([])
    const navigate = useNavigate()
    const handleTextFieldChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value } = event.currentTarget;
        setState({ ...state, [name]: value })
        console.log('state', state)
    }

    return (
        <div className={classes.create}>
            <div className={classes.header}>
                <div className={classes.unsetButton}>
                    <Link to='/patientsDirectory'>
                        <ArrowCircleLeft />
                    </Link>
                    Добавить новой записи
                </div>
                <div>
                    {
                        PatientsDirectoryEditActions.map((item, index) => (
                            <Button
                                size="large"
                                variant="contained"
                                className={classes.header_actions}
                                key={index}
                                data-type={item.dataset}
                                onClick={e => {
                                    e.currentTarget.dataset.type === 'remove' ? navigate('/patientsDirectory') : console.log('clicked')
                                }}
                                color={item.text === 'Отмена' ? 'error' : 'primary'}
                            >
                                {item.icon}
                                {item.text}
                            </Button>
                        ))
                    }
                </div>
            </div>
            <Grid container spacing={2}>
                <Grid xs={6} md={4}>
                    <h3 className={classes.title}>Персональная информация</h3>
                    <Grid container spacing={2}>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField name='id' onChange={handleTextFieldChange} label="ID клиента" type="text" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField onChange={handleTextFieldChange} name='med_number' label="Номер мед.карты" type="number" />
                            </FormControl>
                        </Grid>
                    </Grid>
                    <FormControl fullWidth className={classes.padding_8}>
                        <TextField label="Дата рождения" type="text" />
                    </FormControl>
                    <FormControl fullWidth className={classes.padding_8}>
                        <TextField label="Имя" type="text" />
                    </FormControl>
                    <FormControl fullWidth className={classes.padding_8}>
                        <TextField label="Фамилия" type="text" />
                    </FormControl>
                    <FormControl fullWidth className={classes.padding_8}>
                        <TextField label="Отчество" type="text" />
                    </FormControl>
                </Grid>

                <Grid xs={6} md={8}>
                    <h3 className={classes.title}>Родитель / Опекун</h3>
                    <Grid container spacing={2}>
                        <Grid md={6}>
                            <FormControl style={{ flexDirection: 'row', alignItems: 'center' }} fullWidth>
                                <FormLabel style={{ marginRight: '40px' }} id="demo-radio-buttons-group-label">Пол</FormLabel>
                                <RadioGroup
                                    style={{ display: 'block' }}
                                    aria-labelledby="demo-radio-buttons-group-label"
                                    defaultValue="male"
                                    name="radio-buttons-group"
                                >
                                    <FormControlLabel value="female" control={<Radio />} label="Женский" />
                                    <FormControlLabel value="male" control={<Radio />} label="Мужской" />
                                </RadioGroup>
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Адрес" type="text" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Домашный телефон" type="number" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Мобилный телефон" type="number" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Электронная почта" type="email" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Дополнительная  информация" type="text" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Создатель пациента" type="text" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Медкарта" type="text" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <TextField label="Депозить" type="text" />
                            </FormControl>
                        </Grid>
                        <Grid md={6}>
                            <FormControl fullWidth>
                                <FormControlLabel control={<Checkbox defaultChecked />} label="Активный" />
                            </FormControl>
                        </Grid>
                    </Grid>
                </Grid>

                <Grid xs={6} md={8}>
                    <Tabber />
                </Grid>

                <Grid xs={6} md={4}>
                    <Button className={classes.secondaryButton} variant="outlined" fullWidth>ЭМК</Button>
                    <Button className={classes.secondaryButton} variant="outlined" fullWidth>Посещения</Button>
                    <Button className={classes.secondaryButton} variant="outlined" fullWidth>Оплаты</Button>
                    <Button className={classes.secondaryButton} variant="outlined" fullWidth>Промокод</Button>
                    <Button className={classes.secondaryButton} variant="outlined" fullWidth>Котракты</Button>
                </Grid>

                <Grid xs={6} md={12} style={{ display: 'flex', justifyContent: 'space-between ' }}>
                    <Button className={`${classes.secondaryButton} ${classes.w50}`} variant="outlined" >Промокод</Button>
                    <Button className={`${classes.secondaryButton} ${classes.w50}`} variant="outlined" >Промокод</Button>
                </Grid>

            </Grid>
        </div >
    );
};

export default CreatePatients;

import React from "react";
import {
    Box,
    Button,
    Checkbox,
    FormControl,
    FormControlLabel,
    FormGroup,
    FormLabel,
    InputLabel,
    MenuItem,
    Modal,
    Paper,
    Radio,
    RadioGroup,
    Select,
    TextField,
    Typography,
} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";
import classes from '../cashboxview.module.scss';


const IncomeOutcomeModal = ({ setIncomeOutcomeModal, incomeOutcomeModal }) => {
    return (
        <Modal
            open={incomeOutcomeModal}
            onClose={() => setIncomeOutcomeModal(false)}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box className={classes.modalWrapper} style={{ width: 800 }}>
                <div className={classes.modalHeader}>
                    <h4>Касса</h4>
                    <button
                        onClick={() => setIncomeOutcomeModal(false)}
                        className={classes.roundedOutlineButton}
                    >
                        <CloseRoundedIcon />
                    </button>
                </div>
                <Box sx={{ flexGrow: 1 }} style={{ padding: "0 24px 24px  " }}>
                    <Grid container spacing={2}>
                        <Grid xs={8} className={classes.flexContainer}>
                            <div className={classes.wrapper50}>
                                <TextField
                                    className={classes.mb10}
                                    id="outlined-basic"
                                    label="Наличными"
                                    variant="outlined"
                                />
                            </div>
                            <div className={classes.wrapper50}>
                                <FormControl className={classes.mb10} fullWidth>
                                    <InputLabel id="demo-simple-select-label">
                                        Форма оплаты{" "}
                                    </InputLabel>
                                    <Select
                                        labelId="demo-simple-select-label"
                                        id="demo-simple-select"
                                        label="Форма оплаты "
                                    >
                                        <MenuItem value={10}>Ten</MenuItem>
                                    </Select>
                                </FormControl>
                            </div>
                            <FormControl className={classes.mb10} fullWidth>
                                <InputLabel id="demo-simple-select-label">К приходу</InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    label="К приходу"
                                >
                                    <MenuItem value={10}>Ten</MenuItem>
                                </Select>
                            </FormControl>
                            <FormControl className={classes.mb10} fullWidth>
                                <InputLabel id="demo-simple-select-label">
                                    Назначение платежа
                                </InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    label="Назначение платежа"
                                >
                                    <MenuItem value={10}>Ten</MenuItem>
                                </Select>
                            </FormControl>
                            <FormControl className={classes.mb10} fullWidth>
                                <InputLabel id="demo-simple-select-label">
                                    Категория платежа
                                </InputLabel>
                                <Select
                                    labelId="demo-simple-select-label"
                                    id="demo-simple-select"
                                    label="Категория платежа"
                                >
                                    <MenuItem value={10}>Ten</MenuItem>
                                </Select>
                            </FormControl>
                            <Box style={{ width: "100%" }}>
                                <FormControl fullWidth>
                                    <FormLabel
                                        style={{ marginBottom: 10 }}
                                        id="demo-row-radio-buttons-group-label"
                                    >
                                        Вид платежа
                                    </FormLabel>
                                    <RadioGroup
                                        row
                                        aria-labelledby="demo-row-radio-buttons-group-label"
                                        name="row-radio-buttons-group"
                                    >
                                        <Paper elevation={2} className={classes.paper}>
                                            <FormControlLabel
                                                style={{ marginRight: 40 }}
                                                value="Приход"
                                                control={<Radio />}
                                                label="Приход"
                                            />
                                            <FormControlLabel
                                                value="Расход"
                                                control={<Radio />}
                                                label="Расход"
                                            />
                                        </Paper>
                                    </RadioGroup>
                                </FormControl>
                            </Box>
                            <FormControl className={classes.mb10} fullWidth>
                                <label>Вид платежа </label>
                                <TextField
                                    multiline
                                    rows={4}
                                    className={classes.mb10}
                                    id="outlined-basic"
                                    label="Наличными"
                                    variant="outlined"
                                />
                            </FormControl>
                            <div style={{ width: "100%" }} className={classes.flexContainer}>
                                <Button className={classes.secondaryButton} variant="outlined" >принять</Button>
                                <Button className={classes.secondaryButton} variant="outlined">Отмена</Button>
                            </div>
                        </Grid>
                        <Grid xs={4}>
                            <Typography>
                                Калькулятор
                            </Typography>
                            <TextField
                                className={classes.mb10}
                                id="outlined-basic"
                                label="Сумма "
                                variant="outlined"
                            />
                            <TextField
                                className={classes.mb10}
                                id="outlined-basic"
                                label="К оплате "
                                variant="outlined"
                            />
                            <TextField
                                className={classes.mb10}
                                id="outlined-basic"
                                label="Сдача "
                                variant="outlined"
                            />
                            <FormGroup>
                                <FormControlLabel control={<Checkbox />} label="Повторяющийся платеж" />
                            </FormGroup>
                        </Grid>
                    </Grid>
                </Box>
            </Box>
        </Modal>
    );
};

export default IncomeOutcomeModal
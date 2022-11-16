import React from "react";
import Notification from "../../components/Notification";
import {
  Button,
  Checkbox,
  FormControl,
  FormControlLabel,
  FormLabel,
  InputLabel,
  MenuItem,
  Radio,
  RadioGroup,
  Select,
  TextField,
} from "@mui/material";
import Grid from "@mui/material/Unstable_Grid2";
import { MobileDatePicker } from "@mui/x-date-pickers";
import { PatientsDirectoryEditActions } from "../../consts/patientsDirectory";
import { ReactComponent as ArrowCircleLeft } from "../../assets/img/arrow-circle-left.svg";
import { useNavigate } from "react-router";
import classes from "../../views/PatientsDirectory/createPatient.module.scss";
import { Link } from "react-router-dom";
import Tabber from "../../views/PatientsDirectory/tabber";

const PatientForm = ({
  handleSelectChange,
  post_patient,
  handleCloseNotification,
  handleChange,
  handleTextFieldChange,
  open,
  value,
  medcard,
  setState,
  state,
  title
}) => {
  const navigate = useNavigate();

  return (
    <>
      <Notification open={open} handleClose={handleCloseNotification} />
      <div className={classes.header}>
        <div className={classes.unsetButton}>
          <Link to="/patientsDirectory">
            <ArrowCircleLeft />
          </Link>
          {title}
        </div>
        <div>
          {PatientsDirectoryEditActions.map((item, index) => (
            <Button
              size="large"
              variant="contained"
              className={classes.header_actions}
              key={index}
              data-type={item.dataset}
              onClick={(e) => {
                e.currentTarget.dataset.type === "remove"
                  ? navigate("/patientsDirectory")
                  : post_patient();
              }}
              color={item.text === "Отмена" ? "error" : "primary"}
            >
              {item.icon}
              {item.text}
            </Button>
          ))}
        </div>
      </div>
      <Grid container spacing={2}>
        <Grid xs={6} md={4}>
          <h3 className={classes.title}>Персональная информация</h3>
          <Grid container spacing={2}>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  name="id"
                  onChange={handleTextFieldChange}
                  label="ID клиента"
                  type="text"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="med_number"
                  label="Номер мед.карты"
                  type="number"
                />
              </FormControl>
            </Grid>
          </Grid>
          <FormControl fullWidth className={classes.padding_8}>
            <MobileDatePicker
              label="Дата рождения "
              inputFormat="MM/DD/YYYY"
              value={value}
              // name='date_of_birth'
              onChange={handleChange}
              renderInput={(params) => <TextField {...params} />}
            />
          </FormControl>
          <FormControl fullWidth className={classes.padding_8}>
            <TextField
              onChange={handleTextFieldChange}
              name="f_name"
              label="Имя"
              type="text"
            />
          </FormControl>
          <FormControl fullWidth className={classes.padding_8}>
            <TextField
              onChange={handleTextFieldChange}
              name="l_name"
              label="Фамилия"
              type="text"
            />
          </FormControl>
          <FormControl fullWidth className={classes.padding_8}>
            <TextField
              onChange={handleTextFieldChange}
              name="mid_name"
              label="Отчество"
              type="text"
            />
          </FormControl>
        </Grid>

        <Grid xs={6} md={8}>
          <h3 className={classes.title}>Родитель / Опекун</h3>
          <Grid container spacing={2}>
            <Grid md={6}>
              <FormControl
                style={{ flexDirection: "row", alignItems: "center" }}
                fullWidth
              >
                <FormLabel
                  style={{ marginRight: "40px" }}
                  id="demo-radio-buttons-group-label"
                >
                  Пол
                </FormLabel>
                <RadioGroup
                  style={{ display: "block" }}
                  aria-labelledby="demo-radio-buttons-group-label"
                  defaultValue="male"
                  name="sex"
                  onChange={handleTextFieldChange}
                >
                  <FormControlLabel
                    value="female"
                    control={<Radio />}
                    label="Женский"
                  />
                  <FormControlLabel
                    value="male"
                    control={<Radio />}
                    label="Мужской"
                  />
                </RadioGroup>
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="address"
                  label="Адрес"
                  type="text"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="home_phone_number"
                  label="Домашный телефон"
                  type="number"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="mobile_phone_number"
                  label="Мобилный телефон"
                  type="number"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="email"
                  label="Электронная почта"
                  type="email"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="additional_info"
                  label="Дополнительная  информация"
                  type="text"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="created_by"
                  label="Создатель пациента"
                  type="number"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Медкарта </InputLabel>
                <Select
                  labelId="demo-simple-select-label"
                  id="demo-simple-select"
                  value={medcard}
                  label="Медкарта "
                  name="med_card"
                  onChange={handleSelectChange}
                >
                  <MenuItem value={"В клинике"}>В клинике</MenuItem>
                  <MenuItem value={"В клинике2"}>В клинике2</MenuItem>
                  <MenuItem value={"В клинике3"}>В клинике3</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <TextField
                  onChange={handleTextFieldChange}
                  name="deposit"
                  label="Депозить"
                  type="text"
                />
              </FormControl>
            </Grid>
            <Grid md={6}>
              <FormControl fullWidth>
                <FormControlLabel
                  control={
                    <Checkbox
                      onChange={handleTextFieldChange}
                      name="is_active"
                      defaultChecked
                    />
                  }
                  label="Активный"
                />
              </FormControl>
            </Grid>
          </Grid>
        </Grid>

        <Grid xs={6} md={8}>
          <Tabber
            state={state}
            setState={setState}
            handleSelectChange={handleSelectChange}
            handleTextFieldChange={handleTextFieldChange}
          />
        </Grid>

        <Grid xs={6} md={4}>
          <Button
            className={classes.secondaryButton}
            variant="outlined"
            fullWidth
          >
            ЭМК
          </Button>
          <Button
            className={classes.secondaryButton}
            variant="outlined"
            fullWidth
          >
            Посещения
          </Button>
          <Button
            className={classes.secondaryButton}
            variant="outlined"
            fullWidth
          >
            Оплаты
          </Button>
          <Button
            className={classes.secondaryButton}
            variant="outlined"
            fullWidth
          >
            Промокод
          </Button>
          <Button
            className={classes.secondaryButton}
            variant="outlined"
            fullWidth
          >
            Котракты
          </Button>
        </Grid>

        <Grid
          xs={6}
          md={12}
          style={{ display: "flex", justifyContent: "space-between " }}
        >
          <Button
            className={`${classes.secondaryButton} ${classes.w50}`}
            variant="outlined"
          >
            Заглавная страница медкарты
          </Button>
          <Button
            className={`${classes.secondaryButton} ${classes.w50}`}
            variant="outlined"
          >
            История звонков
          </Button>
        </Grid>
      </Grid>
    </>
  );
};

export default PatientForm;

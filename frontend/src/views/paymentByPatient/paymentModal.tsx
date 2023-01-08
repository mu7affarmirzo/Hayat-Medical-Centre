import {
  Box,
  Button,
  Checkbox,
  FormControl,
  FormControlLabel,
  FormLabel,
  InputLabel,
  MenuItem,
  Modal,
  Paper,
  Radio,
  RadioGroup,
  Select,
  TextField,
} from "@mui/material";
import React from "react";
import classes from "./paymentModal.module.scss";
import table from "./paymentByPatient.module.scss";
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";
import Grid from "@mui/material/Unstable_Grid2";
import BpCheckbox from "../../components/BpCheckbox";
import payment from "../../repositories/data/payments.json";
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";
import { currencyFormatter } from "../../utils/currencyFormatter";

const PaymentModal = ({ open, close, selectedReceipt }) => {
  const [paymentType, setPaymentType] = React.useState<string>("Приход");
  const [handleOpenChild, setHandleOpenChild] = React.useState<boolean>(false);
  console.log('selectedReceipt', selectedReceipt)
  const handleChangePaymentType = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setPaymentType((event.target as HTMLInputElement).value);
  };
  return (
    <Modal
      open={open}
      onClose={close}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      {selectedReceipt && (<Box className={classes.modalWrapper} style={{ width: 1400 }}>
        <div className={classes.modalHeader}>
          <h4>Оплата</h4>
          <button onClick={close} className={classes.roundedOutlineButton}>
            <CloseRoundedIcon />
          </button>
        </div>
        <div className={classes.modalBody}>
          <Box sx={{ flexGrow: 1 }}>
            <Grid container spacing={2}>
              <Grid xs={3}>
                <h4 className={`${classes.formSubtitle} ${classes.mb10}`}>
                  Форма оплаты
                </h4>
                <FormControl fullWidth className={classes.mb10}>
                  <InputLabel id="demo-simple-select-label">
                    Вид платежа
                  </InputLabel>
                  <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    label="Вид платежа"
                  >
                    <MenuItem value={"Банковская карта"}>
                      Банковская карта
                    </MenuItem>
                    <MenuItem value={"Наличные"}>Наличные</MenuItem>
                  </Select>
                </FormControl>
                <FormControlLabel
                  className={classes.mb10}
                  control={<Checkbox />}
                  label="Вручную"
                />
                <FormControl fullWidth className={classes.mb10}>
                  <TextField label="Сумма" />
                </FormControl>
                <FormControl fullWidth>
                  <RadioGroup
                    row
                    onChange={handleChangePaymentType}
                    aria-labelledby="demo-row-radio-buttons-group-label"
                    name="row-radio-buttons-group"
                    value={paymentType}
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
                <FormControlLabel
                  className={classes.mb10}
                  control={<Checkbox />}
                  label="Безналичный расчёт"
                />
                <FormControl fullWidth>
                  <TextField label="DK ФИО или ID номер" />
                </FormControl>
              </Grid>
              <Grid xs={9}>
                <FormControlLabel
                  className={classes.mb10}
                  control={<Checkbox defaultChecked />}
                  label="Выбрать всё"
                />
                <Box className={classes.tableWrapper}>
                  <table className={table.table}>
                    <thead className={table.tableHead}>
                      {[
                        "",
                        "Тип услуги",
                        "Наименования услуги",
                        "Опер сумма",
                        "Скидка",
                        "Долг",
                        "Цена итого",
                      ].map((item) => (
                        <th key={item}>{item}</th>
                      ))}
                    </thead>
                    {selectedReceipt.receipt_appointments[0].services.map((item) => (
                      <tr>
                        <td
                          style={{ display: "flex", justifyContent: "center" }}
                        >
                          <BpCheckbox
                            id={item.id}
                            style={{ padding: "15.5px " }}
                            // handlecheckboxchange={handlecheckboxchange}
                            defaultChecked={false}
                          />
                        </td>
                        <td>{item.type_payment}</td>
                        <td>{item.service_name}</td>
                        <td>{currencyFormatter(selectedReceipt.receipt_appointments[0].price, 'uzs')}</td>
                        <td>{currencyFormatter(selectedReceipt.receipt_appointments[0].discount, 'uzs')}</td>
                        <td>{currencyFormatter(selectedReceipt.receipt_appointments[0].debt, 'uzs')}</td>
                        <td>{item.payment_date}</td>
                      </tr>
                    ))}
                  </table>
                </Box>
                <Box className={classes.flexContainer}>
                  <FormControl style={{ maxWidth: 180, marginRight: 10 }}>
                    <FormLabel id="demo-row-radio-buttons-group-label">
                      Вид платежа
                    </FormLabel>
                    <TextField
                      placeholder="Какой то текст"
                      multiline
                      rows={4}
                    />
                  </FormControl>
                  <div style={{ width: "100%" }}>
                    <FormLabel>История оплаты</FormLabel>
                    <table className={`${table.table} ${classes.elipsis}`}>
                      <thead className={table.tableHead}>
                        {[
                          "",
                          "Тип услуги",
                          "Операционист",
                          "Сумма",
                          "Направления",
                          "Дата/время",
                          "Форма оплаты",
                          "Комментарий",
                        ].map((item) => (
                          <th key={item}>{item}</th>
                        ))}
                      </thead>
                      {payment.slice(0, 2).map((item) => (
                        <tr>
                          <td
                            style={{
                              display: "flex",
                              justifyContent: "center",
                            }}
                          >
                            <BpCheckbox
                              id={item.id}
                              style={{ padding: "15.5px " }}
                              // handlecheckboxchange={handlecheckboxchange}
                              defaultChecked={false}
                            />
                          </td>
                          <td>
                            <span>{item.service}</span>
                          </td>
                          <td>
                            <span>{item.speciality}</span>
                          </td>
                          <td>
                            <span>{item.speciality}</span>
                          </td>
                          <td>
                            <span>{item.speciality}</span>
                          </td>
                          <td>
                            <span>{item.speciality}</span>
                          </td>
                          <td>
                            <span>{item.speciality}</span>
                          </td>
                          <td>
                            <span>{item.speciality}</span>
                          </td>
                        </tr>
                      ))}
                    </table>
                  </div>
                </Box>
                <Box
                  sx={{
                    display: "flex",
                    justifyContent: "flex-end",
                    marginTop: "10px",
                  }}
                >
                  <Button
                    sx={{ marginRight: 1 }}
                    variant="contained"
                    onClick={() => setHandleOpenChild(true)}
                  >
                    {paymentType}
                  </Button>
                  <Button onClick={close} variant="outlined">
                    Отмена
                  </Button>
                </Box>
              </Grid>
            </Grid>
          </Box>
        </div>
        <Modal open={handleOpenChild} onClose={() => setHandleOpenChild(false)}>
          <>
            <Box
              className={`${classes.modalWrapper} ${classes.childModal}`}
              style={{ width: 450 }}
            >
              <h3>Успешно выполнено</h3>
              <div>
                <InfoOutlinedIcon />
                Оплата была проведена успешно
              </div>
              <Button onClick={() => setHandleOpenChild(false)}>OK</Button>
            </Box>
          </>
        </Modal>
      </Box>)}
    </Modal>
  );
};

export default PaymentModal;

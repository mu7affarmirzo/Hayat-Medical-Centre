import { Box, Button, ButtonGroup, TextField } from "@mui/material";
import React from "react";
import Grid from "@mui/material/Unstable_Grid2";
import classes from "./paymentByPatient.module.scss";
import payment from "../../repositories/data/payments.json";
import PaymentModal from "./paymentModal";
import { CASHIER_ACTIONS } from "../../consts/main";

const PaymentByPatientView = ({
  handleSelectPatient,
  selected,
  paymentModal,
  setPaymentModal,
}) => {
  return (
    <div style={{ width: "100%" }}>
      <ButtonGroup className={classes.actionButtonsWrapper}>
        {CASHIER_ACTIONS.map((button, index) => (
          <Button key={index} className={classes.headerActionButton}>
            {button.img}
            <span>{button.title}</span>
          </Button>
        ))}
      </ButtonGroup>
      <div className={classes.wrapper}>
        <Box sx={{ flexGrow: 1 }}>
          <Grid container spacing={2}>
            <Grid xs={6}>
              <TextField
                fullWidth
                id="outlined-basic"
                label="Номер счёта"
                variant="outlined"
              />
            </Grid>
            <Grid xs={6}>
              <TextField
                fullWidth
                id="outlined-basic"
                label="Пациент"
                variant="outlined"
              />
            </Grid>
          </Grid>
          <h3 className={classes.title}>Неоплаченные услуги клиента</h3>
        </Box>
        <table className={classes.table}>
          <thead className={classes.tableHead}>
            {[
              "",
              "Пациент",
              "Врач",
              "Услуга",
              "Дата услуги",
              "Тип услуги",
              "Долг",
              "Цена",
              "Скидка",
              "Филиал",
              "DK",
            ].map((item) => (
              <th key={item}>{item}</th>
            ))}
          </thead>
          <tbody>
            {payment.map((item, index) => (
              <tr
                key={item.id}
                data-id={item.id}
                onClick={handleSelectPatient}
                className={
                  selected === String(item.id) ? classes.selected : null
                }
              >
                <td></td>
                <td>{item.payment_date}</td>
                <td>{item.doctor}</td>
                <td>{item.speciality}</td>
                <td>{item.service}</td>
                <td>{item.type_payment}</td>
                <td>{item.patient}</td>
                <td>{item.base_price}</td>
                <td>{item.comment}</td>
                <td>{item.amount_payment}</td>
                <td>{item.bank}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <PaymentModal
          open={paymentModal}
          close={() => setPaymentModal(false)}
        />
      </div>
    </div>
  );
};

export default PaymentByPatientView;

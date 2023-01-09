import { Box, Button, ButtonGroup, TextField } from "@mui/material";
import React from "react";
import Grid from "@mui/material/Unstable_Grid2";
import classes from "./paymentByPatient.module.scss";
import PaymentModal from "./paymentModal";
import { CASHIER_ACTIONS } from "../../consts/main";
import { IReceipt } from "../../consts/types";
import { generate_date } from "../../utils/dateFormatter";
import { currencyFormatter } from "../../utils/currencyFormatter";

const PaymentByPatientView = ({
  handleSelectPatient,
  selected,
  paymentModal,
  setPaymentModal,
  receipts,
  selectedReceipt,
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
            {receipts.map((item: IReceipt, index: number) => (
              <tr
                key={item.id}
                data-id={item.id}
                onClick={e => handleSelectPatient(e, item)}
                className={
                  selected === String(item.id) ? classes.selected : null
                }
              >
                <td></td>
                <td>{item.receipt_appointments[0]?.patient_name}</td>
                <td>{item.receipt_appointments[0]?.doctor_name}</td>
                <td>{item.receipt_appointments[0]?.services[0].service_name}</td>
                <td>{generate_date(new Date(item.receipt_appointments[0]?.services[0]?.created_at ?? new Date()))}</td>
                <td>{item.receipt_appointments[0]?.services[0]?.payment_status ?? ''}</td>
                <td>{currencyFormatter(item.receipt_appointments[0]?.debt ?? 0, 'UZS')}</td>
                <td>{currencyFormatter(item.receipt_appointments[0]?.price ?? 0, 'UZS')}</td>
                <td>{item.receipt_appointments[0]?.discount ?? 0 + '%'}</td>
                <td>{item.receipt_appointments[0]?.branch}</td>
                <td>{item.receipt_appointments[0]?.referring_doctor}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {selectedReceipt && <PaymentModal
          open={paymentModal}
          selectedReceipt={selectedReceipt}
          close={() => setPaymentModal(false)}
        />}
      </div>
    </div>
  );
};

export default PaymentByPatientView;

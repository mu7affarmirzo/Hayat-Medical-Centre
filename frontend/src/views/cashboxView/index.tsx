import React from "react";
import {
  Button,
  ButtonGroup,
  FormControl,
  Input,
  InputAdornment,
  TextField,
} from "@mui/material";
import SearchIcon from "@mui/icons-material/Search";
import Box from "@mui/material/Box";
import classes from "./cashboxview.module.scss";
import { ReactComponent as LockImage } from "../../assets/img/header_icons/lock.svg";
import { ReactComponent as Export } from "../../assets/img/header_icons/bill.svg";
import BpCheckbox from "../../components/BpCheckbox";
import PaymentDeletionModal from "./Modals/PaymentDeletionModal";
import IncomeOutcomeModal from "./Modals/IncomeOutcomeModal";
import PaymentModal from "./Modals/PaymentModal";
import { generate_date } from "../../utils/dateFormatter";
import { ITransaction } from "../../consts/types";
import { currencyFormatter } from "../../utils/currencyFormatter";

const NAVBAR_BUTTONS = [
  // {
  //   name: "Закрыть кассу",
  //   img: <LockImage />,
  //   type: "close_cash",
  // },
  {
    name: "Закрыть кассу пункта",
    img: <Export />,
    type: "close_cash_punkt",
  },
  {
    name: "Экспорть в Excel",
    img: <LockImage />,
    type: "expoert_to_excel",
  },
  {
    name: "Приход/ Расход",
    img: <LockImage />,
    type: "income_outcome",
  },
  {
    name: "Свод по суммам",
    img: <LockImage />,
    type: "detailed_total_sum",
  },
];
const CashboxView = ({
  navbarActionHandler,
  paymentActionHandler,
  transactions,
  sumPaymentModal,
  deletePaymentModal,
  selectedPayment,
  incomeOutcomeModal,
  setIncomeOutcomeModal,
  setDeletePaymentModal,
  setSumPaymentModal,
}) => {
  return (
    <>
      <div className={classes.wrapper}>
        <nav className={classes.navbar}>
          <Box component={"form"} className={classes.navbarInputs}>
            <TextField
              id="outlined-basic"
              label="Сумма в касса нал"
              variant="outlined"
            />
            <TextField
              id="outlined-basic"
              label="Сумма в касса безнал"
              variant="outlined"
            />
          </Box>
          <ButtonGroup color="primary" className={classes.navbarButtonGroup}>
            {NAVBAR_BUTTONS.map((button, index) => (
              <Button
                key={index}
                onClick={navbarActionHandler}
                data-action-type={button.type}
              >
                {button.img}
                <span>{button.name}</span>
              </Button>
            ))}
          </ButtonGroup>
        </nav>
        {transactions.length > 0 && (<div>
          <h4 className={classes.title}>
            Незакрытые платежи по филиалу Головной
          </h4>
          <div className={classes.patientsList}>
            <FormControl className={classes.searchbox} variant="standard">
              <Input
                placeholder="Введите текст для поиска..."
                id="input-with-icon-adornment"
                endAdornment={
                  <InputAdornment position="end">
                    <SearchIcon />
                  </InputAdornment>
                }
              />
            </FormControl>

            <table className={classes.table}>
              <thead className={classes.tableHead}>
                {[
                  "",
                  "Дата платежа",
                  "Врач",
                  "Специалность",
                  "Услуга",
                  "Вид платежа",
                  "Клиент",
                  "Базовая цена",
                  "Комментарий",
                  "Сумма платежа  ",
                  "Банк",
                  "Безнал",
                  "Назначения платежа",
                  "Направление платежа",
                  "№ чека",
                ].map((item) => (
                  <th key={item}>{item}</th>
                ))}
              </thead>
              <tbody>
                {transactions.map((item: ITransaction, index) => (
                  <tr
                    key={item.id}
                    data-payment-id={item.id}
                    onClick={paymentActionHandler}
                    className={`${parseInt(selectedPayment) === item.id
                      ? classes.selected
                      : null
                      } ${classes.tableRow}`}
                  >
                    <td></td>
                    <td>{generate_date(new Date(item.created_at))}</td>
                    <td>{item.doctor.username}</td>
                    <td>{item.specialty.name}</td>
                    <td>{item.service.name}</td>
                    <td>{item.payment_type}</td>
                    <td>{item.patient.name}</td>
                    <td>{currencyFormatter(item.base_price ?? 0, 'UZS')}</td>
                    <td>{item.comment}</td>
                    <td>{currencyFormatter(item.amount ?? 0, 'UZS')}</td>
                    <td>{item.bank}</td>
                    <td>
                      <BpCheckbox id={item.id} defaultChecked={false} />
                    </td>
                    <td>{item.payment_purpose}</td>
                    <td>{item.transaction_type}</td>
                    <td>{item.receipt_id}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>)}
        {!!transactions.length && (
          <Box className={classes.overall}>
            <TextField
              value={currencyFormatter(transactions.flatMap((item: ITransaction) => item.amount).reduce((sum, acc) => sum + acc, 0), 'UZS')}
              id="outlined-basic"
              label="Приход"
              variant="outlined"
            />
            <TextField
              defaultValue={"10 861 958,17"}
              id="outlined-basic"
              label="Расход"
              variant="outlined"
            />
            <TextField
              defaultValue={"83 017 442,57"}
              id="outlined-basic"
              label="Сумма"
              variant="outlined"
            />
          </Box>
        )}
      </div>
      <PaymentDeletionModal
        setDeletePaymentModal={setDeletePaymentModal}
        deletePaymentModal={deletePaymentModal}
        transactions={transactions}
      />
      <PaymentModal
        sumPaymentModal={sumPaymentModal}
        setSumPaymentModal={setSumPaymentModal}
      />
      <IncomeOutcomeModal
        setIncomeOutcomeModal={setIncomeOutcomeModal}
        selectedReceipt={transactions.filter(transaction => transaction.id === parseInt(selectedPayment))[0]}
        incomeOutcomeModal={incomeOutcomeModal}
      />
    </>
  );
};

export default CashboxView;

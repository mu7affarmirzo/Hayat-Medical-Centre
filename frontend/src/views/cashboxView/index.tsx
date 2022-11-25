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
import React from "react";
import classes from "./cashboxview.module.scss";
import { ReactComponent as LockImage } from "../../assets/img/header_icons/lock.svg";
import { ReactComponent as Export } from "../../assets/img/header_icons/bill.svg";
import payment from "../../repositories/data/payments.json";
import BpCheckbox from "../../components/BpCheckbox";
import PaymentDeletionModal from "./Modals/PaymentDeletionModal";
import IncomeOutcomeModal from "./Modals/IncomeOutcomeModal";
import PaymentModal from "./Modals/PaymentModal";

const NAVBAR_BUTTONS = [
  {
    name: "Закрыть кассу",
    img: <LockImage />,
    type: "close_cash",
  },
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
const CashboxView = () => {
  const [selectedPayment, setSelectedPayment] = React.useState<string>("");
  const [incomeOutcomeModal, setIncomeOutcomeModal] =
    React.useState<boolean>(false);
  const [deletePaymentModal, setDeletePaymentModal] =
    React.useState<boolean>(false);
  const [sumPaymentModal, setSumPaymentModal] = React.useState<boolean>(false);

  const navbarActionHandler = (e: React.MouseEvent<HTMLButtonElement>) => {
    console.log(e.currentTarget.dataset.actionType);
    switch (e.currentTarget.dataset.actionType) {
      case "close_cash_punkt":
        setDeletePaymentModal(true);
        break;
      case "detailed_total_sum":
        setSumPaymentModal(true);
        break;
      case "income_outcome":
        setIncomeOutcomeModal(true);
        break;

      default:
        break;
    }
  };

  const paymentActionHandler = (e: React.MouseEvent<HTMLElement>) => {
    setSelectedPayment(e.currentTarget.dataset?.paymentId ?? "");
  };

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
        <div>
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
                {payment.map((item, index) => (
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
                    <td>
                      <BpCheckbox id={item.id} defaultChecked={false} />
                    </td>
                    <td>{item.payment_purpose}</td>
                    <td>{item.direction_of_payment}</td>
                    <td>{item.cheque}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
        <Box className={classes.overall}>
          <TextField
            defaultValue={"69 188 142,01"}
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
      </div>
      <PaymentDeletionModal
        setDeletePaymentModal={setDeletePaymentModal}
        deletePaymentModal={deletePaymentModal}
        selectedPayment={selectedPayment}
      />
      <PaymentModal
        sumPaymentModal={sumPaymentModal}
        setSumPaymentModal={setSumPaymentModal}
      />
      <IncomeOutcomeModal
        setIncomeOutcomeModal={setIncomeOutcomeModal}
        incomeOutcomeModal={incomeOutcomeModal}
      />
    </>
  );
};



export default CashboxView;

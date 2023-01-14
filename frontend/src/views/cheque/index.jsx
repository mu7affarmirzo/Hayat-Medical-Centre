import React, { useRef } from "react";
import { Navigate } from "react-router";
import classes from "./cheque.module.scss";
import HayatLogo from "../../assets/img/ekm.svg";
import { Button } from "@mui/material";
import PrintIcon from "@mui/icons-material/Print";
import DownloadIcon from "@mui/icons-material/Download";
import { HomeOutlined } from "@mui/icons-material";
import QRCode from "react-qr-code";
import CashboxStateKeeper from "../../store/CashboxStateKeeper";
import { useLocalObservable } from "mobx-react-lite";
import { generate_date } from "../../utils/dateFormatter";
import Barcode from "react-barcode";

const Cheque = () => {
  const chequeRef = useRef(null);
  const cashboxStateKeeper = useLocalObservable(
    () => CashboxStateKeeper.instance
  );
  const { cheque } = cashboxStateKeeper;
  if (cheque.receipt_appointments === undefined) return <Navigate to="/" />;
  return (
    <div className={classes.wrapper}>
      <div className={classes.cheque} ref={chequeRef}>
        <div className={classes.header}>
          <div className={classes.QRwrapper}>
            <QRCode
              size={64}
              style={{ height: "auto", maxWidth: "100%", width: "100%" }}
              value={
                "https://www.google.com/maps/place/hayat+medical+centre/@41.3669729,69.3321519,17z/data=!3m1!4b1!4m5!3m4!1s0x38aef37d53b13691:0x8c2edec291de12b7!8m2!3d41.3669729!4d69.3343406"
              }
              viewBox={`0 0 256 256`}
            />
            <QRCode
              size={64}
              style={{ height: "auto", maxWidth: "100%", width: "100%" }}
              value={"https://hayatmed.uz/"}
              viewBox={`0 0 256 256`}
            />
          </div>
          <img src={HayatLogo} alt="" className={classes.logo} />
          <p className={classes.hayatInfo}>
            Ташкентская область, <br />
            Кибрайский район,
            <br />
            ул. Мевазор, 5/14
            <br />
            +998 71 -200-88-66,
            <br />
            www.Hayatmed.uz
            <br />
            Telegram +998-97-442-30-70
          </p>
        </div>
        <h2 className={classes.textCenter}>Счёт к оплате </h2>
        <div className={classes.flex}>
          <h3 className={classes.textRow}>
            Пациент: {cheque.receipt_appointments[0].patient_name}
          </h3>
          <div>
            <h3 className={classes.textRow}>Номер счета: {cheque.id}</h3>
            <Barcode width={1} value="theakbarov.t.me" />
          </div>
        </div>
        <h3 className={classes.textRow}>
          Дата рождения:{" "}
          {generate_date(
            new Date(cheque.receipt_appointments[0].patient_birth_date)
          )}
        </h3>
        {cheque.receipt_appointments[0].referring_doctor && (
          <h3 className={classes.textRow}>
            Направил: {cheque.receipt_appointments[0].referring_doctor}
          </h3>
        )}
        <h3 className={`${classes.textRow} ${classes.dashedBorder}`}>
          Дата приёма: {generate_date(new Date(cheque.created_at))}
        </h3>
        <table className={classes.table}>
          <th>Называния услуги </th>
          <th>Врач </th>
          <th>Цена </th>
          <tbody>
            {cheque.receipt_appointments.map((appointment) =>
              appointment.services.map((item) => (
                <tr>
                  <td>{item.service_name} </td>
                  <td>{appointment.doctor_name} </td>
                  <td>{appointment.debt} </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
        <h3 className={classes.textRow}>
          Итого:{" "}
          {cheque.receipt_appointments
            .flatMap((item) => item.debt)
            .reduce((sum, acc) => sum + acc, 0)}
        </h3>
        <h3 className={classes.textRow}>Очередь: ____</h3>
        <br />
        <br />
        <p className="paragraph">
          Все вышеперечисленные услуги и моя информация верны, и я согласен с
          предоставляемыми услугами:
        </p>
        <br />
        <p className="paragraph">
          Yuqoridagi barcha xizmatlar va mening ma'lumotlarim to'g'ri
          ko'rsatilgan va men taqdim etilgan xizmatlarga qo'shilaman:
          _____________________ (Imzo/Подпись)
        </p>
      </div>
      <div className={classes.actions}>
        <Button variant="contained">
          <HomeOutlined />
          Hа главную
        </Button>
        <div>
          <Button variant="contained">
            <DownloadIcon />
            Скачать
          </Button>
          <Button variant="outlined">
            <PrintIcon />
            Распечатать
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Cheque;

import { Box, TextField } from '@mui/material'
import React from 'react'
import Grid from '@mui/material/Unstable_Grid2';
import classes from './paymentByPatient.module.scss'
import payment from "../../repositories/data/payments.json";

const PaymentByPatientView = () => {
    return (
        <div className={classes.wrapper}>
            <Box sx={{ flexGrow: 1 }} >
                <Grid container spacing={2}>
                    <Grid xs={6}>
                        <TextField fullWidth id="outlined-basic" label="Номер счёта" variant="outlined" />
                    </Grid>
                    <Grid xs={6}>
                        <TextField fullWidth id="outlined-basic" label="Пациент" variant="outlined" />
                    </Grid>
                </Grid>
                <h3 className={classes.title}>Неоплаченные услуги клиента</h3>
            </Box>
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
                            </td>
                            <td>{item.payment_purpose}</td>
                            <td>{item.direction_of_payment}</td>
                            <td>{item.cheque}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default PaymentByPatientView
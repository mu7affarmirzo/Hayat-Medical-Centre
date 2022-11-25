import {
    Box,
    Modal,
} from "@mui/material";
import React from 'react';
import classes from '../cashboxview.module.scss';
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";


const PaymentModal = ({ sumPaymentModal, setSumPaymentModal }) => {
    return (
        <Modal
            open={sumPaymentModal}
            onClose={() => setSumPaymentModal(false)}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box className={classes.modalWrapper} style={{ width: 450 }}>
                <div className={classes.modalHeader}>
                    <h4>Касса</h4>
                    <button
                        onClick={() => setSumPaymentModal(false)}
                        className={classes.roundedOutlineButton}
                    >
                        <CloseRoundedIcon />
                    </button>
                </div>
                <table className={classes.table}>
                    <thead style={{ background: "#64B6F7" }}>
                        <th></th>
                        <th>Вид платежа</th>
                        <th>Сумма</th>
                    </thead>
                    <tbody>
                        <tr>
                            <td></td>
                            <td>Payme</td>
                            <td>Payme</td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>Payme</td>
                            <td>Payme</td>
                        </tr>
                        <tr>
                            <td></td>
                            <td>Payme</td>
                            <td>Payme</td>
                        </tr>
                    </tbody>
                </table>
            </Box>
        </Modal>
    );
};
export default PaymentModal
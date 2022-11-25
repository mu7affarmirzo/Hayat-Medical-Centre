import React from 'react';
import {
    Button,
    Modal,
    Typography,
} from "@mui/material";
import { Stack } from "@mui/system";
import { ReactComponent as PrintIcon } from "../../../assets/img/printer.svg";
import Box from "@mui/material/Box";
import classes from '../cashboxview.module.scss';
import CloseRoundedIcon from "@mui/icons-material/CloseRounded";
import payment from "../../../repositories/data/payments.json";

const PaymentDeletionModal = ({
    setDeletePaymentModal,
    deletePaymentModal,
    selectedPayment,
}) => {
    return (
        <Modal
            open={deletePaymentModal}
            onClose={() => setDeletePaymentModal(false)}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
        >
            <Box className={classes.modalWrapper} style={{ width: 600 }}>
                <div className={classes.modalHeader}>
                    <h4>Касса</h4>
                    <button
                        onClick={() => setDeletePaymentModal(false)}
                        className={classes.roundedOutlineButton}
                    >
                        <CloseRoundedIcon />
                    </button>
                </div>
                <div className={classes.waringWrapper}>
                    <Typography
                        className={classes.modalContentTitle}
                        variant="h5"
                        component="h6"
                    >
                        Закрыть кассу{" "}
                        {selectedPayment &&
                            payment.filter((pay) => pay.id === parseInt(selectedPayment))[0]
                                .amount_payment}{" "}
                        ?
                    </Typography>
                </div>
                <Stack
                    width={"100%"}
                    direction="row"
                    spacing={14}
                    style={{ margin: "20px 24px" }}
                >
                    <Button
                        onClick={() => window.print()}
                        className={classes.secondaryButton}
                        variant="outlined"
                    >
                        <PrintIcon />
                        Печать чека
                    </Button>
                    <Stack direction="row" spacing={2}>
                        <Button className={classes.secondaryButton} variant="outlined">
                            Закрыть кассу
                        </Button>
                        <Button
                            onClick={() => setDeletePaymentModal(false)}
                            className={classes.secondaryButton}
                            variant="outlined"
                        >
                            Отменить
                        </Button>
                    </Stack>
                </Stack>
            </Box>
        </Modal>
    );
};
export default PaymentDeletionModal
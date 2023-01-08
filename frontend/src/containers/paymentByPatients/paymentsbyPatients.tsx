import { useLocalObservable } from "mobx-react-lite";
import React, { useEffect, useState } from "react";
import { IReceipt } from "../../consts/types";
import TransactionsStateKeeper from "../../store/TransactionStateKeeper";
import PaymentByPatientView from "../../views/paymentByPatient/paymentByPatientView";

const PaymentsbyPatientsContainer = () => {
    const [selected, setSelected] = React.useState<string>("");
    const [paymentModal, setPaymentModal] = React.useState<boolean>(false);
    const [selectedReceipt, setSelectedReceipt] = useState<IReceipt>()
    const handleSelectPatient = (event: React.MouseEvent<HTMLElement>, receipt: IReceipt) => {
        setSelected(event.currentTarget.dataset.id || "");
        setSelectedReceipt(receipt)
        setPaymentModal(true);
    };
    const [receipts, setReceipts] = useState<IReceipt[]>([])

    const transactionsStateKeeper = useLocalObservable(
        () => TransactionsStateKeeper.instance
    )

    useEffect(() => {
        transactionsStateKeeper.findAllReceipts().then(res => setReceipts(res))
    }, [])
    return (
        <PaymentByPatientView
            paymentModal={paymentModal}
            setPaymentModal={setPaymentModal}
            handleSelectPatient={handleSelectPatient}
            selectedReceipt={selectedReceipt}
            receipts={receipts}
            selected={selected}
        />
    );
};

export default PaymentsbyPatientsContainer;

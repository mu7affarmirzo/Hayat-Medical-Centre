import { useLocalObservable } from "mobx-react-lite";
import React, { useEffect } from "react";
import TransactionsStateKeeper from "../../store/TransactionStateKeeper";
import CashboxView from "../../views/cashboxView";

const CashBoxContainer = () => {
    const [selectedPayment, setSelectedPayment] = React.useState<string>("");
    const [incomeOutcomeModal, setIncomeOutcomeModal] =
        React.useState<boolean>(false);
    const [deletePaymentModal, setDeletePaymentModal] =
        React.useState<boolean>(false);
    const [sumPaymentModal, setSumPaymentModal] = React.useState<boolean>(false);

    const transactionsStateKeeper = useLocalObservable(
        () => TransactionsStateKeeper.instance
    )
    const { transactions, findAllTransactions } = transactionsStateKeeper

    useEffect(() => {
        findAllTransactions().then()
    }, [findAllTransactions])

    const navbarActionHandler = (e: React.MouseEvent<HTMLButtonElement>) => {
        switch (e.currentTarget.dataset.actionType) {
            case "close_cash_punkt":
                if (selectedPayment.length > 0) {
                    setDeletePaymentModal(true);
                }
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
        <CashboxView
            selectedPayment={selectedPayment}
            incomeOutcomeModal={incomeOutcomeModal}
            deletePaymentModal={deletePaymentModal}
            setIncomeOutcomeModal={setIncomeOutcomeModal}
            setDeletePaymentModal={setDeletePaymentModal}
            setSumPaymentModal={setSumPaymentModal}
            sumPaymentModal={sumPaymentModal}
            navbarActionHandler={navbarActionHandler}
            paymentActionHandler={paymentActionHandler}
        />
    );
};

export default CashBoxContainer;

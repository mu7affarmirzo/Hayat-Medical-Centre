import React from "react";
import PaymentByPatientView from "../../views/paymentByPatient/paymentByPatientView";

const PaymentsbyPatientsContainer = () => {
    const [selected, setSelected] = React.useState<string>("");
    const [paymentModal, setPaymentModal] = React.useState<boolean>(false);
    const handleSelectPatient = (event: React.MouseEvent<HTMLElement>) => {
        setSelected(event.currentTarget.dataset.id || "");
        setPaymentModal(true);
    };
    return (
        <PaymentByPatientView
            paymentModal={paymentModal}
            setPaymentModal={setPaymentModal}
            handleSelectPatient={handleSelectPatient}
            selected={selected}
        />
    );
};

export default PaymentsbyPatientsContainer;

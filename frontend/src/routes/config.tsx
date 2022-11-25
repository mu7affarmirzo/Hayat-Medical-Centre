import {LoginContainer, MainContainer} from "../containers/index";
import React, {ReactElement} from "react";
import CreateNote from "../views/createNote/createNote";
import DirectoryContainer from "../containers/directory/DirectoryContainer";
import CreatePatients from "../views/PatientsDirectory/createPatients";
import { Navigate } from "react-router";
import EditPatient from "../views/PatientsDirectory/editPatient";
import CashBoxContainer from "../containers/cashbox/cashBoxContainer";
import PaymentsbyPatientsContainer from "../containers/paymentByPatients/paymentsbyPatients";

type IRouting = {
    path: string;
    component: ReactElement,
    global?: boolean
}

type MyGroupType = {
    [key: string]: Array<IRouting>;
}

export const RoutingData: MyGroupType = {
    "NoAuth": [
        {
            "path": "/login",
            "component": <LoginContainer/>,
            "global": true,
        },
    ],
    "admin": [
        {
            "path": "/",
            "component": <Navigate to='/main' />,
            "global": true,
        },
        {
            "path": "/main",
            "component": <MainContainer/>,
            "global": true,
        },
        {
            "path": "/createNote",
            "component": <CreateNote/>,
        },
        {
            "path": "/patientsDirectory",
            "component": <DirectoryContainer />,
        },
        {
            "path": "/patientsDirectory/create",
            "component": <CreatePatients />,
        },
        {
            "path": "/patientsDirectory/edit/:id",
            "component": <EditPatient />,
        },
        {
            "path": "/cashbox",
            "component": <CashBoxContainer />
        },
        {
            "path": "/patientPayments",
            "component": <PaymentsbyPatientsContainer />
        }
    ]
};
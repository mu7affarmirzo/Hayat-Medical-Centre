import {LoginContainer, MainContainer} from "../containers/index";
import React, {ReactElement} from "react";
import CreateNote from "../views/createNote/createNote";
import DirectoryContainer from "../containers/directory/DirectoryContainer";
import CreatePatients from "../views/PatientsDirectory/createPatients";

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
            "component": <CreatePatients />,
        },
    ]
};
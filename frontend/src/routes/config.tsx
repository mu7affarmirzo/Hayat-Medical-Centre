import {LoginContainer, MainContainer} from "../containers/index";
import React, {ReactElement} from "react";

type IRouting = {
    path: string;
    component: ReactElement,
    global?: boolean
}

type MyGroupType = {
    [key:string]: Array<IRouting>;
}

export const RoutingData: MyGroupType = {
    "NoAuth": [
        {
            "path": "/login",
            "component": <LoginContainer />,
            "global": true,
        },
    ],
    "test": [
        {
            "path": "/test",
            "component": <MainContainer />,
            "global": true,
        }
    ]
};
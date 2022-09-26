import React from 'react';
import {Navigate, Route, Routes} from "react-router";
import {RoutingData} from "./consts/main";
import {observer} from 'mobx-react-lite';
import AuthorizationStore from "./store/authorization"

const AppRouting = observer(() => {
    let role = AuthorizationStore.role;

    if(!RoutingData[role]){
        throw new Error(`This type "${role}" of role is not defined `);
    }

    return (
        <Routes>
            {
                RoutingData[role].map((item, i) => {
                    return (
                        <>
                            <Route key={i} path={item.path} element={item.component} />

                            {
                                item.global && <Route path="*" element={<Navigate to={item.path} replace />} />
                            }
                        </>
                    );
                })
            }
        </Routes>
    );
});

export default AppRouting;
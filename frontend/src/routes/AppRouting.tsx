import React from 'react';
import {Navigate, Route, Routes} from "react-router";
import {RoutingData} from "./config";
import {observer} from 'mobx-react-lite';
import AuthorizationStore from "../store/authorization";
import Headers from "../components/headers";
import styles from "../views/main/index.module.scss";
import SideBar from "../components/sideBar";

const AppRouting = observer(() => {
    let role = AuthorizationStore.role;

    if(!RoutingData[role]){
        throw new Error(`This type "${role}" of role is not defined `);
    }

    return (
        <>


            {
                role !== "NoAuth"
                ?
                    <>
                        <Headers/>
                        <div className={styles.main_wrapper}>
                            <SideBar />

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
                        </div>

                    </>
                :
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
            }
        </>
    );
});

export default AppRouting;
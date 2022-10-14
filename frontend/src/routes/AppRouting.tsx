import React, {useEffect} from 'react';
import {Navigate, Route, Routes} from "react-router";
import {RoutingData} from "./config";
import {observer, useLocalObservable} from 'mobx-react-lite';
import Headers from "../components/headers";
import styles from "../views/main/index.module.scss";
import SideBar from "../components/sideBar";
import {AuthorizationStateKeeper} from "../store";

const AppRouting = observer(() => {

    const authorizationStateKeeper = useLocalObservable(() => AuthorizationStateKeeper.instance);
    const {role} = authorizationStateKeeper;

    useEffect(() => {
        if (!RoutingData[role]) {
            throw new Error(`This type "${role}" of role is not defined `);
        }
    }, [role]);

    return (
        <>


            {
                role !== "NoAuth"
                    ?
                    <>
                        <Headers/>
                        <div className={styles.main_wrapper}>
                            <SideBar/>

                            <Routes>
                                {
                                    RoutingData[role].map((item, i) => {
                                        return (
                                            <>
                                                <Route key={i} path={item.path} element={item.component}/>

                                                {
                                                    item.global &&
                                                    <Route path="*" element={<Navigate to={item.path} replace/>}/>
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
                                        <Route key={i} path={item.path} element={item.component}/>

                                        {
                                            item.global &&
                                            <Route path="*" element={<Navigate to={item.path} replace/>}/>
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
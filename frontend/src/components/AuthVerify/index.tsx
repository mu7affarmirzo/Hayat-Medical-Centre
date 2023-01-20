import axios from "axios";
import { useLocalObservable } from "mobx-react-lite";
import React, { useEffect } from "react";
import { useLocation } from "react-router-dom";
import AuthorizationStateKeeper from "../../store/AuthorizationStateKeeper";

const parseJwt = (token) => {
    try {
        return JSON.parse(atob(token.split(".")[1]));
    } catch (e) {
        return null;
    }
};

const AuthVerify = () => {
    let location = useLocation();
    const localAuthorizationStateKeeper = useLocalObservable(
        () => AuthorizationStateKeeper.instance
    );
    const { setToken, removeToken, removeRole } = localAuthorizationStateKeeper;

    useEffect(() => {
        if (window.localStorage.getItem("token")) {
            let user: any
            try {
                if (window.localStorage.getItem('token')) {
                    user = JSON.parse(window.localStorage.getItem("token") ?? '');
                    if (user) {
                        const decodedJwt = parseJwt(user.access);
                        if (decodedJwt.exp * 1000 < Date.now()) {
                            axios.post('https://back.dev-hayat.uz/api/v1/token/refresh/', { refresh: user.refresh })
                                .then(res => {
                                    const data = res.data.access;
                                    data.refresh = user.refresh;
                                    setToken(JSON.stringify(data))
                                    window.localStorage.setItem('token', JSON.stringify(data))
                                })
                                .catch(err => console.log(err))
                        }
                    }
                } else {
                    removeToken()
                    removeRole()
                }
            } catch (error) {
                removeToken()
                removeRole()
            }

        }
    }, [location]);

    return <></>;
};

export default AuthVerify;
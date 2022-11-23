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
    const { setToken } = localAuthorizationStateKeeper;

    useEffect(() => {
        if (window.localStorage.getItem("token")) {
            const user = JSON.parse(window.localStorage.getItem("token") ?? '');

            if (user) {
                const decodedJwt = parseJwt(user.access);
                if (decodedJwt.exp * 1000 < Date.now()) {
                    axios.post('https://back.dev-hayat.uz/api/v1/token/refresh/', { refresh: user.refresh })
                        .then(res => {
                            const data = res.data;
                            data.refresh = user.refresh;
                            setToken(JSON.stringify(data))
                        })
                        .catch(err => console.log(err))
                }
            }
        }
    }, [location]);

    return <></>;
};

export default AuthVerify;
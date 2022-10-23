import React, {useState} from 'react';
import {LoginView} from "../../views";
import {ILoginState} from "../../consts/types";
import {useLocalObservable} from "mobx-react-lite";
import {CalendarEventStateKeeper} from "../../store";
import AuthorizationStateKeeper from "../../store/AuthorizationStateKeeper";

const LoginContainer = () => {
    const [values, setValues] = useState<ILoginState>({
        login: '',
        password: '',
        showPassword: false,
        isLoginValid: null,
        isPasswordValid: null,
        rememberMe: false
    });
    const [errorClient, setErrorClient] = useState<boolean>(false);
    const localAuthorizationStateKeeper = useLocalObservable(() => AuthorizationStateKeeper.instance);
    const {setRole} = localAuthorizationStateKeeper;

    const handleChange = (prop: keyof ILoginState) => (event: React.ChangeEvent<HTMLInputElement>) => {
        setValues({...values, [prop]: event.target.value});
    };

    const checkInput = (event: React.ChangeEvent<HTMLInputElement>, type: string) => {
        let value: string = event.target.value;

        if (type === "login") {
            setValues({...values, isLoginValid: value.length > 3})
        } else if (type === "password") {
            setValues({...values, isPasswordValid: value.length > 3})
        }

    }

    const handleClickShowPassword = () => {
        setValues({
            ...values,
            showPassword: !values.showPassword,
        });
    };

    const handleMouseDownPassword = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();
    };

    const loginAction = (event: React.MouseEvent) => {
        setRole("admin")
    }

    return (
        <>
            <LoginView
                values={values}
                setValues={setValues}
                checkInput={checkInput}
                handleChange={handleChange}
                handleClickShowPassword={handleClickShowPassword}
                handleMouseDownPassword={handleMouseDownPassword}
                errorClient={errorClient}
                loginAction={loginAction}
            />
        </>
    );
};

export default LoginContainer;
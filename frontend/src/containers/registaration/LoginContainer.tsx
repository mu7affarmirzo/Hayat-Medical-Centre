import React from 'react';
import {LoginView} from "../../views";
import {ILoginState} from "../../consts/types";

const LoginContainer = () => {
    const [values, setValues] = React.useState<ILoginState>({
        login: '',
        password: '',
        showPassword: false,
        isLoginValid: null,
        isPasswordValid: null,
        rememberMe: false
    });

    const handleChange = (prop: keyof ILoginState) => (event: React.ChangeEvent<HTMLInputElement>) => {
        setValues({...values, [prop]: event.target.value});
    };

    const checkInput = (event:  React.ChangeEvent<HTMLInputElement>, type: string) => {
        let value:string = event.target.value;

        if(type === "login"){
            setValues({...values, isLoginValid: value.length > 3})
        }else if(type === "password"){
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

    return (
        <>
            <LoginView
                values={values}
                setValues={setValues}
                checkInput={checkInput}
                handleChange={handleChange}
                handleClickShowPassword={handleClickShowPassword}
                handleMouseDownPassword={handleMouseDownPassword}
            />
        </>
    );
};

export default LoginContainer;
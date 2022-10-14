import React from 'react';
import {
    Box,
    Button,
    Checkbox,
    Container,
    FormControl,
    FormControlLabel,
    FormGroup,
    FormHelperText,
    Grid,
    IconButton,
    InputAdornment,
    InputLabel,
    Link,
    OutlinedInput,
    Typography
} from "@mui/material"
import {CloseOutlined, ErrorOutlineOutlined, Visibility, VisibilityOff} from '@mui/icons-material';
import {styled} from '@mui/material/styles';
import loginPhoto from "../../assets/img/login_foto.png";
import styles from "./index.module.scss"

const Item = styled(Box)(({theme}) => ({
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
    // backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
    // ...theme.typography.body2,
    // padding: theme.spacing(1),
    // textAlign: 'center',
    // color: theme.palette.text.secondary,
}));

const Login = () => {

    interface State {
        login: string;
        password: string;
        showPassword: boolean;
        isLoginValid: boolean | null;
        isPasswordValid: boolean | null;
        rememberMe: boolean;
    }

    const [values, setValues] = React.useState<State>({
        login: '',
        password: '',
        showPassword: false,
        isLoginValid: null,
        isPasswordValid: null,
        rememberMe: false
    });

    const handleChange = (prop: keyof State) => (event: React.ChangeEvent<HTMLInputElement>) => {
        setValues({...values, [prop]: event.target.value});
    };

    // useEffect(() => {
    //     console.log(values)
    // }, [values])

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

    return (
        <Container maxWidth="xl" sx={{height: "100vh"}}>
            <Grid container spacing={0}>
                <Grid item xl={7} height={"100%"}>
                    <Item height="100vh">
                        <Box sx={{
                            width: "581px",
                        }}>
                            <Typography variant={"interFont"} component="div" className={styles.form_title}>
                                Вход в систему MIS
                                <Typography variant={"interFont"} component="span" className={styles.subtitle}>
                                    Hayat Medical Center
                                </Typography>
                            </Typography>


                            {/*<FormControl control={<TextField label="Логин" variant="outlined" className={styles.input} size="medium"/>} />*/}

                            <FormGroup>
                                <FormControl error={values.isLoginValid === false} className={styles.input}
                                             variant="outlined">
                                    <InputLabel>Логин</InputLabel>

                                    <OutlinedInput
                                        type='text'
                                        label="Логин"
                                        value={values.login}
                                        onChange={handleChange('login')}
                                        onBlur={(e: any) => checkInput(e, "login")}
                                    />

                                    {values.isLoginValid === false &&
                                        <FormHelperText error>
                                            Incorrect entry.
                                        </FormHelperText>
                                    }
                                </FormControl>

                                <FormControl error={values.isPasswordValid === false} className={styles.input}
                                             variant="outlined">
                                    <InputLabel htmlFor="outlined-adornment-password">Пароль</InputLabel>
                                    <OutlinedInput
                                        id="outlined-adornment-password"
                                        type={values.showPassword ? 'text' : 'password'}
                                        value={values.password}
                                        onChange={handleChange('password')}
                                        onBlur={(e: any) => checkInput(e, "password")}
                                        endAdornment={
                                            <InputAdornment position="end">
                                                <IconButton
                                                    aria-label="toggle password visibility"
                                                    onClick={handleClickShowPassword}
                                                    onMouseDown={handleMouseDownPassword}
                                                    edge="end"
                                                >
                                                    {values.showPassword ? <VisibilityOff/> : <Visibility/>}
                                                </IconButton>
                                            </InputAdornment>
                                        }
                                        label="Password"
                                    />

                                    {values.isPasswordValid === false &&
                                        <FormHelperText error>
                                            Incorrect entry.
                                        </FormHelperText>
                                    }
                                </FormControl>

                                {false && <Box className={`${styles.error_block}`}>
                                    <div className={styles.left_side}>
                                        <ErrorOutlineOutlined sx={{color: "#fff"}}/>
                                        <Typography component={"span"}>
                                            Логин или пароль введен неправильно
                                        </Typography>
                                    </div>
                                    <CloseOutlined sx={{color: "#fff"}}/>
                                </Box>}

                                <Item
                                    sx={{justifyContent: "space-between", paddingRight: "16px", marginBottom: "30px"}}>
                                    <FormControlLabel
                                        control={
                                            <Checkbox
                                                sx={{height: "40px"}}
                                                onChange={(event: any) => setValues({
                                                    ...values,
                                                    rememberMe: event.target.checked
                                                })}
                                            />
                                        }
                                        label="Запомните пароль"
                                    />

                                    <Link href="#/" underline="none" color="primary" fontWeight="500">
                                        Забыли пароль ?
                                    </Link>
                                </Item>


                                <Button
                                    sx={{height: "42px"}}
                                    disabled={!(values.isLoginValid === true && values.isPasswordValid === true)}
                                    color="primary"
                                    variant="contained"
                                >
                                    Вход в систему
                                </Button>
                            </FormGroup>


                        </Box>
                    </Item>
                </Grid>
                <Grid item xl={5} height={"100%"}>
                    <Box height="100vh">
                        <img src={loginPhoto} alt="login_photo" className={styles.login_photo}/>
                    </Box>
                </Grid>
            </Grid>
        </Container>
    );
};

export default Login;
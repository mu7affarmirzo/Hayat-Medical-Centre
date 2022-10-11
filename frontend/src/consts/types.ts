export interface ILoginState {
    login: string;
    password: string;
    showPassword: boolean;
    isLoginValid: boolean | null;
    isPasswordValid: boolean | null;
    rememberMe: boolean;
}

export interface ISpecialities {
    id: string;
    name: string;
    color: string
}

export interface IDoctors {
    id: string;
    full_name: string;
    speciality: ISpecialities;
    number: string;
    color: string;
    active: boolean;
}
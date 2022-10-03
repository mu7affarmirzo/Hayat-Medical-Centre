export interface ILoginState {
    login: string;
    password: string;
    showPassword: boolean;
    isLoginValid: boolean | null;
    isPasswordValid: boolean | null;
    rememberMe: boolean;
}
import {makeAutoObservable} from "mobx";

class AuthorizationStateKeeper {

    static _instance: AuthorizationStateKeeper;

    static get instance() {
        if (!AuthorizationStateKeeper._instance) {
            AuthorizationStateKeeper._instance = new AuthorizationStateKeeper();
        }
        return AuthorizationStateKeeper._instance;
    }

    private getRoleFromLocalStorage (): string {
        return localStorage.getItem("role") || "NoAuth"
    }

    role: string = this.getRoleFromLocalStorage();

    constructor() {
        makeAutoObservable(this, {}, {autoBind: true});
    }

    setRole(data: string) {
        localStorage.setItem("role", data)
        this.role = data;
    }

}

export default AuthorizationStateKeeper;


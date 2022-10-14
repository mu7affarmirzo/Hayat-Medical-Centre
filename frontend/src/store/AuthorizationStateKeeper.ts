import {makeAutoObservable} from "mobx";

class AuthorizationStateKeeper {

    static _instance: AuthorizationStateKeeper;

    static get instance() {
        if (!AuthorizationStateKeeper._instance) {
            AuthorizationStateKeeper._instance = new AuthorizationStateKeeper();
        }
        return AuthorizationStateKeeper._instance;
    }

    role: string = "test";

    constructor() {
        makeAutoObservable(this, {}, {autoBind: true});
    }

    setRole(data: string) {
        this.role = data;
    }

}

export default AuthorizationStateKeeper;


import {makeAutoObservable} from "mobx";

class AuthorizationStore {
    role: string = "test";

    constructor() {
        makeAutoObservable(this);
    }

    setRole (data: string) {
        this.role = data;
    }

}

export default new AuthorizationStore();
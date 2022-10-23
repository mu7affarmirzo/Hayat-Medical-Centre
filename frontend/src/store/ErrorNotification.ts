import {makeAutoObservable} from "mobx";
class ErrorNotification {

    openNotification: boolean = false

    static _instance: ErrorNotification;

    static get instance() {
        if (!ErrorNotification._instance) {
            ErrorNotification._instance = new ErrorNotification();
        }
        return ErrorNotification._instance;
    }

    constructor() {
        makeAutoObservable(this, {}, {autoBind: true});
    }

    changeVisibilityNotification (show: boolean) {
        this.openNotification = show;
    }


}

export default ErrorNotification;
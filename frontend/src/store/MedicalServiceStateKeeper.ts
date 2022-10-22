import {makeAutoObservable, runInAction} from "mobx";
import {MedicalSevicesApiStub} from "../repositories";
import {IMedicalService} from "../consts/types";

class MedicalServiceStateKeeper {

    static _instance: MedicalServiceStateKeeper;
    private readonly medicalServiceApiStub: MedicalSevicesApiStub;

    static get instance() {
        if (!MedicalServiceStateKeeper._instance) {
            MedicalServiceStateKeeper._instance = new MedicalServiceStateKeeper();
        }
        return MedicalServiceStateKeeper._instance;
    }

    services: IMedicalService[] = [];

    constructor(
        calendarEventApiStub: MedicalSevicesApiStub = MedicalSevicesApiStub.instance
    ) {
        this.medicalServiceApiStub = calendarEventApiStub;
        makeAutoObservable(this, {}, {autoBind: true});
    }

    async findAllServices(): Promise<IMedicalService[]> {
        const services = await this.medicalServiceApiStub.findAllServices();
        runInAction(() => {
            this.services = services;
        });
        return services;
    }
}

export default MedicalServiceStateKeeper;
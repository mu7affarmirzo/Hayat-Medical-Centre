import {makeAutoObservable, runInAction} from "mobx";
import {DoctorApiStub} from "../repositories";
import {IDoctor} from "../consts/types";

class DoctorStateKeeper {

    static _instance: DoctorStateKeeper;
    private readonly doctorApiStub: DoctorApiStub;

    doctors: IDoctor[] = [];
    selectedDoctor: IDoctor | null = null;
    selectedDoctors: IDoctor[] = [];

    static get instance() {
        if (!DoctorStateKeeper._instance) {
            DoctorStateKeeper._instance = new DoctorStateKeeper();
        }
        return DoctorStateKeeper._instance;
    }

    constructor(
        doctorApiStub: DoctorApiStub = DoctorApiStub.instance
    ) {
        this.doctorApiStub = doctorApiStub;
        makeAutoObservable(this, {}, {autoBind: true});
    }

    async findAllDoctors(): Promise<IDoctor[]> {
        const doctors = await this.doctorApiStub.findAllDoctors();
        runInAction(() => {
            this.doctors = doctors;
        });
        return doctors;
    }

    setSelectedDoctor(doctor: IDoctor) {
        this.selectedDoctor = doctor;
    }

    setSelectedDoctors(doctors: IDoctor[]) {
        this.selectedDoctors = doctors;
    }
}

export default DoctorStateKeeper;


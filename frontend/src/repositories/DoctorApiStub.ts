import {ApiClient} from "../utils";

import doctorsList from "../repositories/data/doctors.json";
import {IDoctor} from "../consts/types";

export default class DoctorApiStub {
    /* Gen by NARA Studio */
    static _instance: DoctorApiStub;

    private readonly client = new ApiClient('/api/doctors');

    static get instance() {
        /* Gen by NARA Studio */
        if (!DoctorApiStub._instance) {
            DoctorApiStub._instance = new DoctorApiStub();
        }
        return DoctorApiStub._instance;
    }

    async findAllDoctors(): Promise<IDoctor[]> {
        /* Gen by NARA Studio */
        return doctorsList ? doctorsList as unknown as IDoctor[] : this.client.getArray<IDoctor>('/');
    }
}

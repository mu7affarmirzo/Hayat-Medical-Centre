import {ApiClient} from "../utils";

import patientsList from "../repositories/data/patients.json";
import {IPatient} from "../consts/types";

export default class PatientApiStub {
  /* Gen by NARA Studio */
  static _instance: PatientApiStub;

  private readonly client = new ApiClient("organizations/patients");

  static get instance() {
    /* Gen by NARA Studio */
    if (!PatientApiStub._instance) {
      PatientApiStub._instance = new PatientApiStub();
    }
    return PatientApiStub._instance;
  }
  async findAllPatients(): Promise<IPatient[]> {
    /* Gen by NARA Studio */
    return this.client.getData<IPatient>("/");
    return patientsList
      ? (patientsList as unknown as IPatient[])
      : this.client.getArray<IPatient>("/");
  }
}

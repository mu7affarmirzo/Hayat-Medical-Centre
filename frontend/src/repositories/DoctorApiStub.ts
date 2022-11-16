import {ApiClient} from "../utils";

import { IDoc } from "../consts/types";

export default class DoctorApiStub {
  /* Gen by NARA Studio */
  static _instance: DoctorApiStub;

  private readonly client = new ApiClient("organizations/doctors");

  static get instance() {
    /* Gen by NARA Studio */
    if (!DoctorApiStub._instance) {
      DoctorApiStub._instance = new DoctorApiStub();
    }
    return DoctorApiStub._instance;
  }

  async findAllDoctors(): Promise<IDoc[]> {
    /* Gen by NARA Studio */
    return this.client.getData<IDoc>("/");
  }
}

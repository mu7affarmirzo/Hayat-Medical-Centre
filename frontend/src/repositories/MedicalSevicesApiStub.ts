import {ApiClient} from "../utils";

import {IMedicalService} from "../consts/types";

export default class MedicalServiceApiStub {
  /* Gen by NARA Studio */
  static _instance: MedicalServiceApiStub;

  private readonly client = new ApiClient("doctors/services");

  static get instance() {
    /* Gen by NARA Studio */
    if (!MedicalServiceApiStub._instance) {
      MedicalServiceApiStub._instance = new MedicalServiceApiStub();
    }
    return MedicalServiceApiStub._instance;
  }

  async findAllServices(): Promise<IMedicalService[]> {
    /* Gen by NARA Studio */
    return this.client.getData<IMedicalService>("/");
    /* 
    return servicesList
    ? (servicesList as unknown as IMedicalService[])
    : this.client.getArray<IMedicalService>("/");
    */
  }
}

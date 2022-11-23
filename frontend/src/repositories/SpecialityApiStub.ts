import {ApiClient} from "../utils";
import { ISpeciality } from "../consts/types";

export default class SpecialityApiStub {
  /* Gen by NARA Studio */
  static _instance: SpecialityApiStub;
  private readonly client = new ApiClient("organizations/specialities");

  static get instance() {
    /* Gen by NARA Studio */
    if (!SpecialityApiStub._instance) {
      SpecialityApiStub._instance = new SpecialityApiStub();
    }
    return SpecialityApiStub._instance;
  }

  async findAllSpecialties(): Promise<ISpeciality[]> {
    /* Gen by NARA Studio */
    return this.client.getData<ISpeciality>("/");
  }
}

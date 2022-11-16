import { ApiClient } from "../utils";

import { IBranch } from "../consts/types";

export default class BranchesApiStub {
  /* Gen by NARA Studio */
  static _instance: BranchesApiStub;

  private readonly client = new ApiClient("organizations/branches");

  static get instance() {
    /* Gen by NARA Studio */
    if (!BranchesApiStub._instance) {
      BranchesApiStub._instance = new BranchesApiStub();
    }
    return BranchesApiStub._instance;
  }

  async findAllBranches(): Promise<IBranch[]> {
    /* Gen by NARA Studio */
    return this.client.getData<IBranch>("/");
  }
}

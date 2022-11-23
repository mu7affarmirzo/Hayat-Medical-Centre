import { makeAutoObservable, runInAction } from "mobx";
import { IBranch } from "../consts/types";
import BranchesApiStub from "../repositories/BranchesApiStub";

class BranchesStateKeeper {
  static _instance: BranchesStateKeeper;
  private readonly branchesApiStub: BranchesApiStub;

  branches: IBranch[] = [];
  branchesCopy: IBranch[] = [];

  static get instance() {
    if (!BranchesStateKeeper._instance) {
      BranchesStateKeeper._instance = new BranchesStateKeeper();
    }
    return BranchesStateKeeper._instance;
  }

  constructor(branchesApiStub: BranchesApiStub = BranchesApiStub.instance) {
    this.branchesApiStub = branchesApiStub;
    makeAutoObservable(this, {}, { autoBind: true });
  }

  async findAllBranches(): Promise<IBranch[]> {
    const branches = await this.branchesApiStub.findAllBranches();
    runInAction(() => {
      this.branches = branches;
      this.branchesCopy = branches;
    });
    return branches;
  }
}

export default BranchesStateKeeper;

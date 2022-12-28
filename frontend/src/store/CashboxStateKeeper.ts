import { makeAutoObservable, runInAction } from "mobx";
import { IReports, ITransaction } from "../consts/types";
import CashboxApiStub from "../repositories/CashboxApiStub";

class CashboxStateKeeper {
  static _instance: CashboxStateKeeper;
  private readonly cashboxApiStub: CashboxApiStub;

  cashbox: ITransaction[] = [];
  reports: IReports[] = [];

  static get instance() {
    if (!CashboxStateKeeper._instance) {
      CashboxStateKeeper._instance = new CashboxStateKeeper();
    }
    return CashboxStateKeeper._instance;
  }
  constructor(cashboxApiStub: CashboxApiStub = CashboxApiStub.instance) {
    this.cashboxApiStub = cashboxApiStub;
    makeAutoObservable(this, {}, { autoBind: true });
  }

  async findAllReports(): Promise<IReports[]> {
    const reports = await this.cashboxApiStub.findAllReports();
    runInAction(() => {
      this.reports = reports;
    });
    return reports;
  }

  async closeHistoryCashbox(data) {
    await this.cashboxApiStub.closeHistory(data);
    return null;

  }

  async findAllTransactions(): Promise<ITransaction[]> {
    const cashbox = await this.cashboxApiStub.findAllCashbox();
    runInAction(() => {
      this.cashbox = cashbox;
    });
    return cashbox;
  }
}
export default CashboxStateKeeper;

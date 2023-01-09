import { ApiClient } from "../utils";
import transactions from "../repositories/data/transactions.json";
import { IReports, ITransaction } from "../consts/types";

export default class CashboxApiStub {
  static _instance: CashboxApiStub;

  private readonly client = new ApiClient("cashbox");

  static get instance() {
    if (!CashboxApiStub._instance) {
      CashboxApiStub._instance = new CashboxApiStub();
    }

    return CashboxApiStub._instance;
  }

  async closeHistory(data) {
    return this.client.postData("/", data);
  }

  async closeCashbox() {
    return this.client.postData("/cashbox", {});
  }

  async findAllReports(): Promise<IReports[]> {
    return this.client.getData("/reports");
  }

  async findAllCashbox(): Promise<ITransaction[]> {
    return transactions
      ? (transactions as unknown as ITransaction[])
      : this.client.getArray<ITransaction>("/");
  }
}

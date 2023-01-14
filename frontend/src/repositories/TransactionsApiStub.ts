import { ApiClient } from "../utils";
import { IReceipt, ITransaction } from "../consts/types";

export default class TransactionsApiStub {
  static _instance: TransactionsApiStub;

  private readonly client = new ApiClient("cashbox");

  static get instance() {
    if (!TransactionsApiStub._instance) {
      TransactionsApiStub._instance = new TransactionsApiStub();
    }

    return TransactionsApiStub._instance;
  }
  async findAllReceipts(): Promise<IReceipt[]> {
    return this.client.getData("/receipt");
  }
  async findAllHistory() {
    return this.client.getData(
      "/cashbox?start_date=2022-01-10&end_date=2023-01-01"
    );
  }
  async findAllTransactions(): Promise<ITransaction[]> {
    return this.client.getData("/transactions/");
  }
}

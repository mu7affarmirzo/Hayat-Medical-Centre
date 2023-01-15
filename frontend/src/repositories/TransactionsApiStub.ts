import { ApiClient } from "../utils";
import { IHistory, IReceipt, ITransaction } from "../consts/types";

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
  async findAllHistory(params: string): Promise<IHistory[]> {
    return this.client.getData(`/cashbox${params}`);
  }
  async findAllTransactions(): Promise<ITransaction[]> {
    return this.client.getData("/transactions/");
  }
}

import { ApiClient } from "../utils";
import transactions from "../repositories/data/transactions.json";
import { ITransaction } from "../consts/types";

export default class TransactionsApiStub {
  static _instance: TransactionsApiStub;

  private readonly client = new ApiClient("/transactions");

  static get instance() {
    if (!TransactionsApiStub._instance) {
      TransactionsApiStub._instance = new TransactionsApiStub();
    }

    return TransactionsApiStub._instance;
  }

  async findAllTransactions(): Promise<ITransaction[]> {
    return transactions
      ? (transactions as unknown as ITransaction[])
      : this.client.getArray<ITransaction>("/");
  }
}

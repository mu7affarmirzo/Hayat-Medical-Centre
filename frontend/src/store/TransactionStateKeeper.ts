import { makeAutoObservable, runInAction } from "mobx";
import { ITransaction } from "../consts/types";
import TransactionsApiStub from "../repositories/TransactionsApiStub";

class TransactionsStateKeeper {
  static _instance: TransactionsStateKeeper;
  private readonly transactionsApiStub: TransactionsApiStub;

  transactions: ITransaction[] = [];

  static get instance() {
    if (!TransactionsStateKeeper._instance) {
      TransactionsStateKeeper._instance = new TransactionsStateKeeper();
    }
    return TransactionsStateKeeper._instance;
  }
  constructor(
    transactionsApiStub: TransactionsApiStub = TransactionsApiStub.instance
  ) {
    this.transactionsApiStub = transactionsApiStub;
    makeAutoObservable(this, {}, { autoBind: true });
  }

  async findAllTransactions(): Promise<ITransaction[]> {
    const transactions = await this.transactionsApiStub.findAllTransactions();
    runInAction(() => {
      this.transactions = transactions;
    });
    return transactions;
  }
}
export default TransactionsStateKeeper;

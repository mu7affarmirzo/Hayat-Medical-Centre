import { makeAutoObservable, runInAction } from "mobx";
import TransactionsApiStub from "../repositories/TransactionsApiStub";
import { IDoc, IReceipt, ITransaction } from "../consts/types";

class TransactionsStateKeeper {
  static _instance: TransactionsStateKeeper;
  private readonly transactionsApiStub: TransactionsApiStub;

  transactions: ITransaction[] = [];
  receipts: IReceipt[] = [];
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

  async findAllReceipts(): Promise<IReceipt[]> {
    const receipts = await this.transactionsApiStub.findAllReceipts();
    runInAction(() => {
      this.receipts = receipts;
    });
    return receipts;
  }

  async findAllTransactions(): Promise<ITransaction[]> {
    const transaction = await this.transactionsApiStub.findAllTransactions();
    runInAction(() => {
      this.transactions = transaction;
    });
    return transaction;
  }
}
export default TransactionsStateKeeper;

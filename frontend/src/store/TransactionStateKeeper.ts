import { makeAutoObservable, runInAction } from "mobx";
import TransactionsApiStub from "../repositories/TransactionsApiStub";
import { IDoc, IHistory, IReceipt, ITransaction } from "../consts/types";

class TransactionsStateKeeper {
  static _instance: TransactionsStateKeeper;
  private readonly transactionsApiStub: TransactionsApiStub;

  transactions: ITransaction[] = [];
  history: IHistory[] = [];
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
  async gethistory(params: string): Promise<IHistory[]> {
    const history = await this.transactionsApiStub.findAllHistory(params);
    runInAction(() => {
      this.history = history;
    });
    return history;
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

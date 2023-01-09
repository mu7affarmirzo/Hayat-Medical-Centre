import { makeAutoObservable, runInAction } from "mobx";
import { IPayment, IPaymentProcess } from "../consts/types";
import PaymentApiStub from "../repositories/PaymentApiStub";

class PaymentStateKeeper {
  static _instance: PaymentStateKeeper;
  private readonly paymentApiStub: PaymentApiStub;

  payments: IPayment[] = [];
  response: any = [];

  static get instance() {
    if (!PaymentStateKeeper._instance) {
      PaymentStateKeeper._instance = new PaymentStateKeeper();
    }
    return PaymentStateKeeper._instance;
  }

  constructor(paymentApiStub: PaymentApiStub = PaymentApiStub.instance) {
    this.paymentApiStub = paymentApiStub;
    makeAutoObservable(this, {}, { autoBind: true });
  }

  async payForPatient(data): Promise<IPaymentProcess[]> {
    const payment = await this.paymentApiStub.payByReceiptId(
      "/transactions/",
      data
    );
    runInAction(() => {
      this.response = payment;
    });
    return this.response;
  }

  async findAllPayments(): Promise<IPayment[]> {
    const payments = await this.paymentApiStub.findAllPayments();
    runInAction(() => {
      this.payments = payments;
    });
    return payments;
  }
}

export default PaymentStateKeeper;

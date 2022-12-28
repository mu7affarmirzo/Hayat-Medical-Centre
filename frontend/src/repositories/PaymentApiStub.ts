import { IPayment } from "../consts/types";
import { ApiClient } from "../utils";
export default class PaymentApiStub {
  static _instance: PaymentApiStub;

  private readonly client = new ApiClient("/");

  static get instance() {
    if (!PaymentApiStub._instance) {
      PaymentApiStub._instance = new PaymentApiStub();
    }
    return PaymentApiStub._instance;
  }

  async findAllPayments(): Promise<IPayment[]> {
    return this.client.getData<IPayment>("");
  }

  async payByReceiptId(data) {
    this.client.postData("/", data);
  }
}

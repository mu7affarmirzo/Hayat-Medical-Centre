import { makeAutoObservable } from "mobx";

class AuthorizationStateKeeper {
  static _instance: AuthorizationStateKeeper;

  static get instance() {
    if (!AuthorizationStateKeeper._instance) {
      AuthorizationStateKeeper._instance = new AuthorizationStateKeeper();
    }
    return AuthorizationStateKeeper._instance;
  }

  private getRoleFromLocalStorage(): string {
    return localStorage.getItem("role") || "NoAuth";
  }

  private getTokensFromLocalStorage(): any {
    return localStorage.getItem("token") || {};
  }
  token: any = this.getTokensFromLocalStorage();
  role: string = this.getRoleFromLocalStorage();

  constructor() {
    makeAutoObservable(this, {}, { autoBind: true });
  }

  setToken(data: any) {
    localStorage.setItem("token", data);
    this.token = data;
  }

  setRole(data: string) {
    localStorage.setItem("role", data);
    this.role = data;
  }
}

export default AuthorizationStateKeeper;

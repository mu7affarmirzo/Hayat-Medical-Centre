import axios from "axios";
import { useLocalObservable } from "mobx-react-lite";
import { AuthorizationStateKeeper } from "../store";

const host = "https://back.dev-hayat.uz/api/v1/";

export default class ApiClient {
  private _url: string;

  constructor(path: string) {
    this._url = `${host}${path}`;
  }
  authorizationStateKeeper = useLocalObservable(
    () => AuthorizationStateKeeper.instance
  );
  token = this.authorizationStateKeeper.token;

  data: any = [];
  response = [];

  async getData<T>(endpoint: string): Promise<T[]> {
    await axios
      .get(this._url + endpoint, {
        headers: {
          Authorization: "Bearer " + JSON.parse(this.token).access,
        },
      })
      .then((response) => {
        this.data = response.data;
      });
    return this.data;
  }

  async postData<T>(endpoint: string, data): Promise<T[]> {
    await axios
      .post(
        this._url + endpoint,
        {
          headers: {
            Authorization: "Bearer " + JSON.parse(this.token).access,
          },
        },
        data
      )
      .then((response) => {
        this.response = response.data;
      });
    return this.response;
  }

  async getArray<T>(endpoint: string): Promise<T[]> {
    const body = (await fetch(`${this._url}${endpoint}`)).body;
    return (Array.isArray(body) ? body : [body]) as T[];
  }
}

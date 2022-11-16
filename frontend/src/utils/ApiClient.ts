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

  async getData<T>(endpoint: string): Promise<T[]> {
    await axios
      .get(this._url + endpoint, {
        headers: {
          Authorization:
            "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY4NjM5NTU1LCJqdGkiOiJmN2I4YTAzZDE4Mjc0MTBmODAyMjdmZDYwNTIxOTRmOCIsInVzZXJfaWQiOjV9.h6SkEJM7jCguE8UxDp_R58GDMZzFugH5w4Bv9YtWmxc",
          // Authorization: "Bearer " + JSON.parse(this.token).access,
        },
      })
      .then((response) => {
        this.data = response.data;
      });
    // const body = (await fetch(`${this._url}${endpoint}`)).body;
    // return (Array.isArray(body) ? body : [body]) as T[];
    return this.data;
  }

  async getArray<T>(endpoint: string): Promise<T[]> {
    const body = (await fetch(`${this._url}${endpoint}`)).body;
    return (Array.isArray(body) ? body : [body]) as T[];
  }
}

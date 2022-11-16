import axios from "axios";

const host = "https://back.dev-hayat.uz/api/v1/";

export default class ApiClient {
  private _url: string;

  constructor(path: string) {
    this._url = `${host}${path}`;
  }
  data: any = [];
  
  async getData<T>(endpoint: string): Promise<T[]> {
    await axios.get(this._url + endpoint).then((response) => {
      this.data = response.data;
    });
    const body = (await fetch(`${this._url}${endpoint}`)).body;
    // return (Array.isArray(body) ? body : [body]) as T[];
    return this.data;
  }

  async getArray<T>(endpoint: string): Promise<T[]> {
    const body = (await fetch(`${this._url}${endpoint}`)).body;
    return (Array.isArray(body) ? body : [body]) as T[];
  }
}

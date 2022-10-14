const host = 'http://localhost:8080';

export default class ApiClient {

    private _url: string;

    constructor(path: string) {
        this._url = `${host}${path}`;
    }

    async getArray<T>(endpoint: string): Promise<T[]> {
        const body = (await fetch(`${this._url}${endpoint}`)).body;
        return (Array.isArray(body) ? body : [body]) as T[];
    }
}
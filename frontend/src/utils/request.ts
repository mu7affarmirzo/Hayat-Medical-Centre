import axios, { AxiosRequestConfig } from "axios";
import jwt_decode from "jwt-decode";
declare module "axios" {
  export interface AxiosRequestConfig {
    handlerEnabled?: boolean;
  }
}
const request = axios.create({ baseURL: "https://back.dev-hayat.uz/api/v1" });

interface Token {
  exp: number;
}

const setToken = (token) => {
  localStorage.setItem("token", token);
};

const isTokenExpired = () => {
  let decoded: Token;
  decoded = jwt_decode(localStorage.getItem("token") ?? "");
  return decoded?.exp > Date.now();
};

const getRefreshedToken = () => {
  return axios.post("/refresh_endpoint");
};

const refreshToken = async () => {
  const newToken = await getRefreshedToken();
  setToken(newToken);
};
console.log(isTokenExpired());

export default request;

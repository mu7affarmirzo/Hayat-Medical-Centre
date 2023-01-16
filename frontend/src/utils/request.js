import axios from "axios";

const request = axios.create({
  baseURL: "https://back.dev-hayat.uz/api/v1/",
});

export default request;

import axios from "axios";
// ..custom
import { API_BASE_URL } from "@/util/envConfig";

// fastapi related instance
export const AudioApiInstance = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// add a request interceptor
AudioApiInstance.interceptors.request.use(
  function (config) {
    // Optional: add Authorization token here if required
    config.headers.Accept = "application/json";
    return config;
  },
  function (err) {
    return Promise.reject(err);
  }
);

// add a response interceptor
AudioApiInstance.interceptors.response.use(
  function (resp) {
    // do something with response data here
    return resp;
  },
  function (err) {
    return Promise.reject(err);
  }
);

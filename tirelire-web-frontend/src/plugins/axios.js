import { useErrorStore } from "@/stores/useError";
import router from "@/router";
import axios from "axios";

axios.defaults.baseURL = "http://localhost:8000/";
axios.defaults.withCredentials = true;


axios.interceptors.request.use(
  function (config) {

    useErrorStore().$reset();

    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  function (response) {
    return response;
  },
  function (error) {
    switch (error.response.status) {
      case 401:
        localStorage.removeItem("token");
        window.location.reload();
        break;
      case 403:
      case 404:
        router.push({
          name: "error",
          props: {
            error: {
              message: error.response.data.message,
              status: error.status,
            },
          },
        });
        break;
      case 422:
        useErrorStore().$state = error.response.data;
        break;
      default:
        console.log(error.response.data);
    }

    return Promise.reject(error);
  }
);

export default axios;
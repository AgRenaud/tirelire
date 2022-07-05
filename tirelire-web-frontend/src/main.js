import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App'
import router from "./router";
import axios from "./plugins/axios";
import auth from "./plugins/auth";

import VueAxios from "vue-axios";

import '@fortawesome/fontawesome-free/js/all'

createApp(App)
    .use(createPinia())
    .use(auth)
    .use(router)
    .use(VueAxios, axios)
    .mount('#app')

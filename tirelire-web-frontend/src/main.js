import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App'
import router from './router'
import axios from 'axios';

import '@fortawesome/fontawesome-free/js/all'

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/'

const app = createApp(App)

app.use(router)
app.use(createPinia())

app.mount('#app')

import { createApp } from 'vue'
import App from './App'
import router from './router'

import '@fortawesome/fontawesome-free/js/all'

const app = createApp(App)

app.use(router)

app.mount('#app')

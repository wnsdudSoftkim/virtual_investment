import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import store from './store/index'
import common from '@/assets/js/common.js'
import 'material-design-icons-iconfont/dist/material-design-icons.css'

async function init() {
    const app = createApp(App)
    app.use(store)
    app.use(router)
    app.use(common)
    app.mount('#app')
}

init()

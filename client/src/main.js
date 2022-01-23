import { createApp } from 'vue'
import App from './App.vue'
import store from 'src/store/index'
import router from 'src/router/index'
createApp(App).mount('#app')


async function init() {
    const app = createApp(App)
    app.use(store)
    app.use(router)
    app.mount('#app')
}

init()

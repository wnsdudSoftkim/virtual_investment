import {createRouter, createWebHistory} from 'vue-router'

const routes= [
    {
    // route config
    path:'/',
    component: ()=> import('@/views/Home')

    }
]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
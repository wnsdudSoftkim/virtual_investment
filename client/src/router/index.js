import {createRouter, createWebHistory} from 'vue-router'

const routes= [
    {
        path:'/',
        component:() => import('@/views/Home')
    },
    {
        // route config
        path:'/store',
        component: ()=> import('@/views/Home')

    }
]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
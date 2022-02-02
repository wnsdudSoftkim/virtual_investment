import {createRouter, createWebHistory} from 'vue-router'
const routes= [
    {
        path:'/',
        component:() => import('@/views/Home')
    },
    {
        // route config
        path:'/chart',
        component: () => import('@/views/Base/BaseChart')
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
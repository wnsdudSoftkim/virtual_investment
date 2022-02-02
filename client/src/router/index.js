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
    },
    {
        // route config
        path:'/chart',
        component: () => import('@/views/Chart/VueChartJS')
    },
    {
        path:'/chart/#progressive',
        component: () => import('@/views/Chart/VueChartJS')
    },
    {
        path:'/chart/#line',
        component: () => import('@/views/fragment/LineFragment.vue')
    },
    {
        path:'/chart/#bar',
        component: () => import('@/views/fragment/BarFragment.vue')
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
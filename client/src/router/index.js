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
        path:'/chartjs',
        component: () => import('@/views/Chart/VueChartJS')
    },
    {
        path:'/chartkick',
        component: () => import('@/views/Chart/VueChartKick')
    },
    {
        path:'/charts',
        component: () => import('@/views/Chart/VueCharts')
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
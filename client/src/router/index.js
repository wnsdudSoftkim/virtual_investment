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
        name: 'VueChartJS',
        componsent: () => import('@/views/VueChartJS')
    },
    {
        path:'/chartkick',
        name: 'VueChartKick',
        componsent: () => import('@/views/VueChartKick')
    },
    {
        path:'/charts',
        name: 'VueChartS',
        componsent: () => import('@/views/VueChartS')
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router
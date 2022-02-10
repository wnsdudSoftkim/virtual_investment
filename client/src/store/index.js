import {createStore} from 'vuex'
import price from '@/store/price'
import header from '@/store/header'
import project from '@/store/project'

const store =  createStore({
    modules: {price, header, project}
})

export default store
import {createStore} from 'vuex'
import price from '@/store/price'
import header from '@/store/header'

const store =  createStore({
    modules: {price, header}
})

export default store
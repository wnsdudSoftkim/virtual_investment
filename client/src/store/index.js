import {createStore} from 'vuex'
import price from '@/store/price'

const store =  createStore({
    modules: {price}
})

export default store
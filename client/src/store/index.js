import {createStore} from 'vuex'
import price from '@/store/price'
import header from '@/store/header'
import project from '@/store/project'
import query from '@/store/query'

const store =  createStore({
    modules: {price, header, project, query}
})

export default store
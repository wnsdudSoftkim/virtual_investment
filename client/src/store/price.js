import SYMBOL from '@/store/mutation-types'

const price = {
    state: () => ({
        symbol: '',
        price:0
    }),
    
    mutations: {
        [SYMBOL.SET_NAME](state, value) {
            state.symbol = value
        }
    },
    getters: {
        symbolInfo(state) {
            return `Symbol name: ${state.symbol}, Price: ${state.price}`
        }
    },
    actions: {
        changeSymbol({commit}, value) {
            console.log('value test',value)
            commit(SYMBOL.SET_NAME, value)
        }
    }
}

export default price
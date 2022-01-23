import {createStore} from 'vuex'

export default createStore({
    state: {
        sampleState: 1
    },
    getters: {
        sampleState: state=> state.sampleState +1
    },
    mutations: {
        sampleState(state, data) {
            state.sampleState = data
        }
    }
})
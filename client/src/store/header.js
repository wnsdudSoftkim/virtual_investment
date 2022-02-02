const price = {
    state: () => ({ headervalue: 0 }),
    mutations: {
      UPDATE_HEADER(state, value) {
        state.headervalue = value;
      }
    },
    actions: {
      updateHeader({commit}, value) {
        commit('UPDATE_HEADER', value)
      }
    },
    getters: {
      updateheader: state =>{
        return state.headervalue
      }
    }
}

export default price
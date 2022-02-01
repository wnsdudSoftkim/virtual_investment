const price = {
    state: () => ({ chartvalue: 10 }),
    mutations: {
      UPDATE_CHART(state, value) {
        state.chartvalue = value;
      }
    },
    actions: {
      updateValue({commit}, value) {
        commit('UPDATE_CHART', value)
      }
    },
    getters: {
      updatechart: state =>{
        return state.chartvalue
      }
    }
}

export default price
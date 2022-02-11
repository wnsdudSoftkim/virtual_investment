const query = {
    state: () => ({ query: {} }),
    mutations: {
      UPDATE_QUERY(state, value) {
        state.query = value;
      }
    },
    actions: {
      updateQuery({commit}, value) {
        commit('UPDATE_QUERY', value)
      }
    },
    getters: {
      updatequery: state =>{
        return state.query
      }
    }
}

export default query
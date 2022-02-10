const project = {
    state: () => ({ project: [{
        title:'',
        description:'',
        profit:'',
    }],
    count:0
}),
    mutations: {
      UPDATE_PROJECT(state, value) {
        value['id'] = state.count
        state.project = state.project.concat(value);
        state.count += 1
      },
      UPDATE_PROFIT(state, value) {
          state.project.profit = value
      }
    },
    actions: {
      updateProject({commit}, value) {
        commit('UPDATE_PROJECT', value)
      },
      updateProfit({commit},value) {
        commit('UPDATE_PROFIT', value)
      }
    },
    getters: {
      updateproject: state =>{
        return state.project
      }
    }
}

export default project
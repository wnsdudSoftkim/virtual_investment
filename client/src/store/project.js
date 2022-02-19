const project = {
    state: () => ({ project: [{
        title:'SAMPLE',
        description:'SAMPLE',
        profit:'',
        quantity:0,
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
          state.project[state.count] = value
      },
      ASC_QUANTITY(state) {
        console.log(state.count)
        console.log(state.project[state.count])
        state.project[state.count].quantity += 1;
      },
      DESC_QUANTITY(state) {
          state.project[state.count].quantity -= 1;
      }
    },
    actions: {
      updateProject({commit}, value) {
        commit('UPDATE_PROJECT', value)
      },
      updateProfit({commit},value) {
        commit('UPDATE_PROFIT', value)
      },
      descQuantity({commit}) {
        commit('DESC_QUANTITY')
      },
      ascQuantity({commit}) {
        commit('ASC_QUANTITY')
      }
    },
    getters: {
      updateproject: state =>{
        return state.project
      },
      getquantity: state =>{
        return state.project[state.count].quantity
      }
    }
}

export default project
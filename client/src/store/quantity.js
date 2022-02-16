const quantity = {
    state: () => ({ quantity: 0 }),
    mutations: {
      ASC_QUANTITY(state) {
        state.quantity += 1;
      },
      DESC_QUANTITY(state) {
          if (state === 0) alert('매도할 물량이 없습니다.')
          state.quantity -= 1;
      }
    },
    actions: {
      descQuantity({commit}) {
        commit('DESC_QUANTITY')
      },
      ascQuantity({commit}) {
          commit('ASC_QUANTITY')
      }

    },
    getters: {
      getquantity: state =>{
        return state.quantity
      }
    }
}

export default quantity
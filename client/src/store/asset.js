const asset = {
    state: () => ({ investasset: 0, priceasset: 0 }),
    mutations: {
      INCREASE_ASSET(state, value) {
        state.investasset += value;
      },
      DECREASE_ASSET(state, value) {
        state.investasset -= value
      },
      UPDATE_PRICE_ASSET(state, value) {
          state.priceasset = value
      }
    },
    actions: {
      IncreaseAsset({commit}, value) {
        commit('INCREASE_ASSET', value)
      },
      DecreaseAsset({commit}, value) {
        commit('DECREASE_ASSET', value)
      },
      UpdatePriceAsset({commit}, value) {
        commit('UPDATE_PRICE_ASSET', value)
      }
    },
    getters: {
      getInvestAsset: state =>{
        return state.investasset
      },
      getPriceAsset: state => {
          return state.priceasset
      }
    }
}

export default asset
const price = {
    state: () => ({ chartvalue: 10, tradeValue:10, priceValue:[], lastDate:'' }),
    mutations: {
      UPDATE_CHART(state, value) {
        state.chartvalue = value;
      },
      UPDATE_TRADE(state, value) {
        state.tradeValue = value
      },
      UPDATE_PRICE(state, value) {
        state.priceValue = value.slice()
      },
      UPDATE_LAST_DATE(state, value) {
        state.lastDate = value
      }
    },
    actions: {
      updateValue({commit}, value) {
        commit('UPDATE_CHART', value)
      },
      updateTrade({commit}, value) {
        commit('UPDATE_TRADE', value)
      },
      updatePrice({commit}, value) {
        commit('UPDATE_PRICE', value)
      },
      updateLastDate({commit}, value) {
        commit('UPDATE_LAST_DATE', value)
      }
    },
    getters: {
      updatechart: state =>{
        return state.chartvalue
      },
      updatetrade: state => {
        return state.tradeValue
      },
      updateprice: state => {
        return state.priceValue
      },
      updatelastdate: state => {
        return state.lastDate
      }
    }
}

export default price
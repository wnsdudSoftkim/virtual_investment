const price = {
    state: () => ({ chartvalue: 10, tradeValue:0, volumeValue:0 ,priceValue:[], lastDate:'', profitRate:0 }),
    mutations: {
      UPDATE_CHART(state, value) {
        state.chartvalue = value;
      },
      UPDATE_TRADE(state, value) {
        state.tradeValue = value
      },
      UPDATE_VOLUME(state, value) {
        state.volumeValue = value
      },
      UPDATE_PRICE(state, value) {
        state.priceValue = value.slice()
      },
      UPDATE_LAST_DATE(state, value) {
        state.lastDate = value
      },
      UPDATE_PROFIT_RATE(state, value) {
        state.profitRate = value
      }
    },
    actions: {
      updateValue({commit}, value) {
        commit('UPDATE_CHART', value)
      },
      updateTrade({commit}, value) {
        commit('UPDATE_TRADE', value)
      },
      updateVolume({commit}, value) {
        commit('UPDATE_VOLUME', value)
      },
      updatePrice({commit}, value) {
        commit('UPDATE_PRICE', value)
      },
      updateLastDate({commit}, value) {
        commit('UPDATE_LAST_DATE', value)
      },
      updateProfitRate({commit}, value) {
        commit('UPDATE_PROFIT_RATE', value)
      }
    },
    getters: {
      updatechart: state =>{
        return state.chartvalue
      },
      updatetrade: state => {
        return state.tradeValue
      },
      updatevolume: state => {
        return state.volumeValue
      },
      updateprice: state => {
        return state.priceValue
      },
      updatelastdate: state => {
        return state.lastDate
      },
      updateprofitrate: state => {
        return state.profitRate
      }
    }
}

export default price
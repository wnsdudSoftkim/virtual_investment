<template>
  <div>
    <h1>Hello World view File</h1>
    {{symbol}}
    {{symbolInfo}}
    <input type="text" :value="name" @input="changeSymbol" placeholder="symbol test"/>
  </div>
</template>

<script>
  import {computed} from 'vue'
  import {useStore} from 'vuex'

  function setPrice() {
    const store = useStore()

    const symbol = computed(() => store.state.price.symbol)  // get state information
    const symbolInfo = computed(() => store.getters['price/symbolInfo']) // get getters
    const changeSymbol = e => store.dispatch('price/changeSymbol', e.target.value) // action method
    
    return {
      symbol, symbolInfo, changeSymbol
    }
  }


  export default {
    setup() {
      return {...setPrice()}
    }
  }


</script>

<style>

</style>
<template>
  <div>
    <h1>Hello World view File</h1>
    {{counter}}
    <!-- {{ times2 }} -->
    <button @click="inc">inc</button>
  </div>
</template>

<script>
import {computed} from 'vue'
import {useStore} from 'vuex'
export default {
  setup() {
    const store = useStore()
    const counter = computed(()=> store.state.sampleState)
    const stateinfo = computed(()=> store.getters)
    const inc = () => store.commit('sampleState', counter.value )
    return {counter, inc, test}
  }
}
</script>

<style>

</style>
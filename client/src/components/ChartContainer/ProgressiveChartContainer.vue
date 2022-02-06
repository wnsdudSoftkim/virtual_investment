<template>
  <div class="container">
    <progressive-chart
      v-if="loaded"
      v-bind:cbvalue="CBVALUE"/>
  </div>
</template>

<script>
import ProgressiveChart from '@/components/Chart/ProgressiveChart'
import methods from '@/assets/js/common.js'
import { useStore } from 'vuex'
export default {
    name: 'ProgressiveChartContainer',
    components: { ProgressiveChart },
    data: function(){
        return {
            loaded: false,
            logs:[],
            cbvalue: [90, 10, 20, 30, 50, 10, 30, 40, 60, 100, 20 , 40],
            status:'disconnected',
            store: useStore()
        }
    }, 
    mounted () {
        try {
            this.loaded = true
        }catch(e) {
            console.log(e)
        }
    },
    computed: {
        CBVALUE() {
            return this.store.getters.updateprice
        }
        // this.cbvalue = this.store.getters.updateprice
    },
    methods: {
        disconnect() {
            methods.chartDisconnect()
        }
    },
}
</script>
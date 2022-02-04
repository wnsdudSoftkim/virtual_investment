<template>
  <div class="container">
    <progressive-chart
      v-if="loaded"
      v-bind:cbvalue="cbvalue"/>
  </div>
</template>

<script>
import ProgressiveChart from '@/components/Chart/ProgressiveChart'
import methods from '@/assets/js/common.js'
import { useStore } from 'vuex'
import {computed} from 'vue'
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
        this.connect()
        try {
            this.loaded = true
        }catch(e) {
            console.log(e)
        }
    },
    methods: {
        connect() {
           this.cbvalue= computed(() => this.store.getters.updatechart)

        },
        disconnect() {
            methods.chartDisconnect()
        }
    }
}
</script>
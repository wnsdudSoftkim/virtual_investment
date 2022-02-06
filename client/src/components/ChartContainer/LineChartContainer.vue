<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      v-bind:cbvalue="cbvalue"/>
  </div>
</template>

<script>
import LineChart from '@/components/Chart/LineChart'
import methods from '@/assets/js/common.js'
import { useStore } from 'vuex'
import {computed} from 'vue'
export default {
    name: 'LineChartContainer',
    components: { LineChart },
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
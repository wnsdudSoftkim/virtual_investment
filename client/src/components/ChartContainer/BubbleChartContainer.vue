<template>
  <div class="container">
    <bubble-chart
      v-if="loaded"
      v-bind:cbvalue="cbvalue"/>
  </div>
</template>

<script>
import BubbleChart from '@/components/Chart/BubbleChart'
import methods from '@/assets/js/common.js'
import { useStore } from 'vuex'
import {computed} from 'vue'
export default {
    name: 'BubbleChartContainer',
    components: { BubbleChart },
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
            /* TODO bubble 차트는 시간대별 매수한 사람이 몇명인지 체크하기위해 변수를 다르게 잡기 */
           this.cbvalue= computed(() => this.store.getters.updatechart)

        },
        disconnect() {
            methods.chartDisconnect()
        }
    }
}
</script>
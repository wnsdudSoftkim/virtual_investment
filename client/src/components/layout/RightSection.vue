<template>
        <div class="columns">
        <div class="column" v-if="this.headervalue == 1" >
            <h3>Base</h3>
            <base-container></base-container>
        </div>
        <div class="column" v-if="this.headervalue == 2" >
            <h3>PRICE</h3>
            <progressive-chart-container></progressive-chart-container>
        </div>
        <div class="column" v-if="this.headervalue == 3">
            <h3>수익률</h3>
            <line-chart-container></line-chart-container>
        </div>
        <div class="column" v-if="this.headervalue == 4">
            <h3>매수한 사람 분포</h3>
            <bubble-chart-container></bubble-chart-container>
        </div>
        <div class="column" v-if="this.headervalue == 5" >
            <h3>Bar Chart</h3>
            <bar-chart-container></bar-chart-container>
        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import ProgressiveChartContainer from '@/components/ChartContainer/ProgressiveChartContainer'
import BubbleChartContainer from '@/components/ChartContainer/BubbleChartContainer'
import BaseContainer from '@/components/ChartContainer/BaseContainer'
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
export default {
    name:'RightSection',
    components: {LineChartContainer, ProgressiveChartContainer, BubbleChartContainer, BaseContainer, BarChartContainer},
    data() {
        return {
  
            datacollection: null,
            store: useStore(),
            chart_data:null,
            server:null,
            headervalue:null,
            count:0,
            firstAsset:10000,
            nowAsset:0,
            profitRate:0
        }
    },
    computed: {
        check_header() {
            return this.store.getters.updateheader
        }
    },
    mounted() {
        this.headervalue = 1
        
    },
    watch: {
        check_header(val) {
            this.headervalue = val
        }
    }
}
</script>

<style>

</style>
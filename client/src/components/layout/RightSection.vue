<template>
    <div class="columns">
        <div class="button-layout">
            <div class="information">
                <reset-button>aa</reset-button>
                <span class="info firstasset">투자금액: <b>{{this.PROPS.firstAsset}}</b> </span>
                <span class="info nowAsset">현재금액: <b>{{this.PROPS.nowAsset}}</b> </span>
                <span class="info profitRate">수익률: <b>{{this.PROPS.profitRate}}%</b></span>
            </div>
        </div>
        <!-- TODO headervalue===1 이면 grid로 바꾸기 -->
        <div class="column" v-if="this.headervalue == 2 || this.headervalue=== 1" >
            <h3>PRICE</h3>
            <progressive-chart-container></progressive-chart-container>
        </div>
        <div class="column" v-if="this.headervalue == 3 || this.headervalue === 1">
            <h3>수익률</h3>
            <line-chart-container></line-chart-container>
        </div>
        <div class="column" v-if="this.headervalue == 4 || this.headervalue === 1">
            <h3>매수한 사람 분포</h3>
            <bubble-chart-container></bubble-chart-container>
        </div>
        <div class="column" v-if="this.headervalue == 5 || this.headervalue === 1" >
            <h3>Bar Chart</h3>
            <bar-chart-container></bar-chart-container>
        </div>
    </div>
</template>

<script>
import { useStore } from 'vuex'
import ResetButton from '@/components/common/button/ResetButton'
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import ProgressiveChartContainer from '@/components/ChartContainer/ProgressiveChartContainer'
import BubbleChartContainer from '@/components/ChartContainer/BubbleChartContainer'
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
export default {
    name:'RightSection',
    components: {ResetButton, LineChartContainer, ProgressiveChartContainer, BubbleChartContainer, BarChartContainer},
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
    props: {
        PROPS:Object
    },
    computed: {
        check_header() {
            return this.store.getters.updateheader
        },

    },
    mounted() {
        this.headervalue = 1
        
    },
    methods: {
        receiveProps() {
            // console.log(this.PROPS)
        }
    },
    watch: {
        check_header(val) {
            this.headervalue = val
        },
        'PROPS': "receiveProps"
    }
}
</script>

<style style="scss">

.button-layout {
    position:absolute;
    top:20%;
    right:8%;
    height:20rem;
    box-shadow: rgba(151, 65, 252, 0.2) 0 15px 30px -5px;
}
.information {
    display: flex;
    flex-direction: column;
}
.info {
    padding:1rem;
    margin:0 auto;
    color:#000;
    font-size:18px;
}
</style>
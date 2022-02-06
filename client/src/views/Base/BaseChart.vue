<template>
    <fragment-layout>
        <reset-button>aa</reset-button>
        <div>시작금액: {{this.firstAsset}} 현재금액: {{this.nowAsset}} 수익률: {{this.profitRate}}%</div>
        <fragment-main-block-layout>
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
        </fragment-main-block-layout>
    </fragment-layout>
</template>

<script>
import ResetButton from '@/components/common/button/ResetButton'
import FragmentLayout from '@/components/layout/FragmentLayout'
import FragmentMainBlockLayout from '@/components/layout/FragmentMainBlockLayout'
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import ProgressiveChartContainer from '@/components/ChartContainer/ProgressiveChartContainer'
import BubbleChartContainer from '@/components/ChartContainer/BubbleChartContainer'
import BaseContainer from '@/components/ChartContainer/BaseContainer'
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
import { useStore } from 'vuex'
import {computed} from 'vue'
import methods from '@/assets/js/common.js'
export default {
    name:'VueChartJS',
    components: { ResetButton, BaseContainer, LineChartContainer, BarChartContainer, BubbleChartContainer, ProgressiveChartContainer , FragmentLayout, FragmentMainBlockLayout },
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
        Chart_Data() {
            return this.chart_data
        },
        check_header() {
            return this.store.getters.updateheader
        }
    },
    mounted() {
        this.headervalue = 1
        this.connect()
        console.log('mount:', this.Chart_Data)
    },
    methods: {
        connect() {
            methods.chartConnect().then((server)=> {
                server.onmessage = ({data}) => {
                    this.server = server
                    const recv = JSON.parse(data)

                    const recv_res = recv['res']

                    const recv_other = recv['other_res']
                    this.count = recv_res.length
                    this.storePrice(recv_res)
                    this.storeDate(recv_res[this.count-1]['x'])
                    this.sendData(recv_res[(this.count)-1]['x'])
                    this.storeTrade(recv_other['trades'])
                    this.storeVolume(recv_other['Volume'])
                    this.nowAsset = recv_other['Open']
                    this.profitRate = (((this.nowAsset-this.firstAsset)/this.firstAsset) * 100).toFixed(2)
                    this.storeprofitRate(this.profitRate)
                }
            }).catch(err=> {
                console.log(err)
            })
        
        },
        sendData(message) { // receive from store value
            methods.sendMessage(message)
        },
        storeTrade(item) {
            this.store.dispatch('updateTrade', item)
        },
        storeVolume(item) {
            this.store.dispatch('updateVolume', item)
        },
        storePrice(item) {
            // this.store.dispatch('updateValue', item)
            this.store.dispatch('updatePrice', item)
        },
        storeDate(item) {
            this.store.dispatch('updateLastDate', item)
        },
        storeprofitRate(item) {
            this.store.dispatch('updateProfitRate', item)
        },
        getData() {
            this.chart_data = computed(() => this.store.getters.updatechart)
        },
        disconnect() {
            console.log(this.server)
            methods.chartDisconnect()
        }
        
    },
    beforeRouteLeave(to, from, next) { 
        this.disconnect()
        next() 
    },
    watch: {
        check_header(val) {
            this.headervalue = val
        }
    }

}
</script>

<style lang="scss">
li {
    display: inline-block;
    margin: 0 1rem;
}
a {
    color:$baseColor;
}

</style>
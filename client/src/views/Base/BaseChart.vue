<template>
    <fragment-layout>
        <reset-button>aa</reset-button>
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
            count:0
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
                    this.count = recv.length
                    this.storePrice(recv)
                    this.storeDate(recv[this.count-1]['x'])
                    this.sendData(recv[(this.count)-1]['x'])
        
                    
                }
            }).catch(err=> {
                console.log(err)
            })
        
        },
        sendData(message) { // receive from store value
            methods.sendMessage(message)
        },
        
        storePrice(item) {
            // this.store.dispatch('updateValue', item)
            this.store.dispatch('updatePrice', item)
        },
        storeDate(item) {
            this.store.dispatch('updateLastDate', item)
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
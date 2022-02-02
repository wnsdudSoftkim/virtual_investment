<template>
    <fragment-layout>
        <fragment-main-block-layout>
             <h1> Demo example of vue-chartjs </h1>
            <div class="columns">
                <div class="column">
                    <h3>Line Chart</h3>
                    <line-chart-container></line-chart-container>
                </div>
                    <div class="column">
                    <h3>Bar Chart</h3>
                    <bar-chart-container></bar-chart-container>
                </div>
                    <div class="column">
                    <h3>Bubble Chart</h3>
                    <bubble-chart></bubble-chart>
                </div>
            </div>
        </fragment-main-block-layout>
    </fragment-layout>
</template>

<script>
import FragmentLayout from '@/components/layout/FragmentLayout'
import FragmentMainBlockLayout from '@/components/layout/FragmentMainBlockLayout'
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
import BubbleChart from '@/components/Chart/BubbleChart'
import { useStore } from 'vuex'
import {computed} from 'vue'
import methods from '@/assets/js/common.js'
export default {
    name:'VueChartJS',
    components: { LineChartContainer, BarChartContainer, BubbleChart , FragmentLayout, FragmentMainBlockLayout },
    data() {
        return {
            datacollection: null,
            store: useStore(),
            chart_data:null,
            server:null
        }
    },
    computed: {
        Chart_Data() {
            return this.chart_data
        }
    },
    mounted() {
        this.connect()
        console.log('mount:', this.Chart_Data)
    },
    methods: {
        connect() {
            methods.chartConnect().then((server)=> {
                server.onmessage = ({data}) => {
                    this.server = server
                    const recv = JSON.parse(data)
                    const value = Math.floor((recv.value * 100))
                    console.log(value)
                    this.storeData(value)
        
                    
                }
            }).catch(err=> {
                console.log(err)
            })
        
        },
        storeData(item) {
            this.store.dispatch('updateValue', item)
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
        // const answer = window.confirm('데이터 저장이 되지 않았습니다. 이 페이지를 나가시겠습니까?') 
        // if (answer) { 
        //     this.disconnect()
        //     next() 
        // } 
        // else { 
        //     next(false)
        // }
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
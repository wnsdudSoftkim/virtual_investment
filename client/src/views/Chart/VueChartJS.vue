<template>
    <div class="container">
        <ul>
            <li>
                <router-link to='/'>Home</router-link>
            </li>
            <li>
                <router-link to='/chartjs'>vue-chartjs</router-link>
            </li>
            <li>
                <router-link to='/charts'>vue-charts</router-link>
            </li>
            <li>
                <router-link to='/chartKick'>vue-chartKick</router-link>
            </li>
        </ul>
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
            <!-- <div class="column">
                <h3>Reactivity - Live update upon change in datasets</h3>
                <reactive :chart-data="datacollection"></reactive>
                <button class="button is-primary" @click="fillData()">Randomize</button>
            </div> -->
        </div>
    </div>
</template>

<script>
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
import BubbleChart from '@/components/Chart/BubbleChart'
import { useStore } from 'vuex'
import {computed} from 'vue'
import methods from '@/assets/js/common.js'
export default {
    name:'VueChartJS',
    components: { LineChartContainer, BarChartContainer, BubbleChart },
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
        const answer = window.confirm('데이터 저장이 되지 않았습니다. 이 페이지를 나가시겠습니까?') 
        if (answer) { 
            this.disconnect()
            next() 
        } 
        else { 
            next(false)
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
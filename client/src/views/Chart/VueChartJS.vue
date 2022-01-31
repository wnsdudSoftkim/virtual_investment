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
                <bar-chart></bar-chart>
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
import BarChart from '@/components/Chart/BarChart'
import BubbleChart from '@/components/Chart/BubbleChart'
// import Reactive from '@/components/Chart/Reactive'
export default {
    name:'VueChartJS',
    components: { LineChartContainer, BarChart, BubbleChart },
    data() {
        return {
            datacollection: null
        }
    },
    created() {
        this.fillData()
    },
    methods: {
        fillData() {
            this.datacollection = {
                 // Data for the y-axis of the chart
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
                'September', 'October', 'November', 'December'],
                datasets: [
                    {
                        label: 'Data One',
                        backgroundColor: '#f87979',
                        // Data for the x-axis of the chart
                        data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
                            this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), 
                            this.getRandomInt(), this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
                    }
                ]
            }
        },
        getRandomInt() {
            return Math.floor(Math.random() * (50 - 5 + 1)) + 5
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
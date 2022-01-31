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
                <line-chart></line-chart>
            </div>
                <div class="column">
                <h3>Bar Chart</h3>
                <bar-chart></bar-chart>
            </div>
                <div class="column">
                <h3>Bubble Chart</h3>
                <bubble-chart></bubble-chart>
            </div>
                <div class="column">
                <h3>Reactivity Line Chart</h3>
                <reactive></reactive>
            </div>
        </div>
    </div>
</template>

<script>
import LineChart from '@/components/Chart/LineChart'
import BarChart from '@/components/Chart/BarChart'
// import BubbleChart from '@/components/Chart/BubbleChart'
// import Reactive from '@/components/Chart/Reactive'
export default {
    components: { LineChart, BarChart },

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
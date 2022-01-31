<template>
    <ul class="chart-ul">
        <!--vue for문으로 바꾸기 -->
        <li class="chart-li">
            <router-link to="/chartjs" class="chart-router">vue-chartjs</router-link>
        </li>
        <li class="chart-li">
            <router-link to="/charts" class="chart-router">vue-charts</router-link>
        </li>
        <li class="chart-li">
            <router-link to="/chartKick" class="chart-router">vue-chartKick</router-link>
        </li>
        <li style="height:100px">
            <line-chart></line-chart>
        </li>
    </ul>

</template>

<script>
import LineChart from '../../Chart/LineChart.vue'
export default {
    component: LineChart
}
</script>

<style lang="scss">
    .chart-ul {
        list-style-type:none;
        padding: 0;
    }
    .chart-li {
        display: flex;
        margin: 0 1rem;
    }
    .chart-router{
        color:$baseColor;
    }

</style>
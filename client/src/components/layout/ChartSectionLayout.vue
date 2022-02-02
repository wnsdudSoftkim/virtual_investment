<template>
    <ul class="chart-ul">
        <!--vue for문으로 바꾸기 -->
        <li class="chart-li">
            <router-link to="/chart" class="chart-router">vue-chartjs</router-link>
        </li>
    </ul>

</template>

<script>
export default {

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
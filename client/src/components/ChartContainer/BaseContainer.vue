<template>
  <div class="container">
      <div class="row">
        <progressive-chart-container></progressive-chart-container>
      </div>
      <div class="row">
        <line-chart-container></line-chart-container>
        <bar-chart-container></bar-chart-container>
        <bubble-chart-container></bubble-chart-container>
      </div>
  </div>
</template>

<script>
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
import ProgressiveChartContainer from '@/components/ChartContainer/ProgressiveChartContainer'
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import BubbleChartContainer from '@/components/ChartContainer/BubbleChartContainer'
export default {
    name: 'BaseContainer',
    components: { BarChartContainer, ProgressiveChartContainer, LineChartContainer, BubbleChartContainer },
}
</script>
<style lang="scss">
.row {
    display: flex;
    justify-content: space-between;
}
</style>
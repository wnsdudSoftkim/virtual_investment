<template>
  <div class="container">
    <line-chart
      v-if="loaded"
      :chartdata="chartdata"
      :options="options"/>
  </div>
</template>

<script>
import LineChart from '@/components/Chart/LineChart'

export default {
  name: 'LineChartContainer',
  components: { LineChart },
  data: () => ({
    loaded: false,
    chartdata: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
            'August', 'September', 'October', 'November', 'December'], 
            datasets:[{
                label: 'Data One',
                backgroundColor: '#f87979',
                pointBackgroundColor: 'white',
                borderWidth: 1,
                pointBorderColor: '#24pEBF',
                data:[40, 20, 30, 50, 90, 10, 20, 40, 50, 70, 90, 100]
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks:{
                        beginAtZero:true
                    },
                    gridLines: {
                        display:true
                    }
                }],
                xAxes: [{
                    gridLines: {
                        display: false
                    }
                }],

            },
            legend: {
                display:true
            },
            responsive: true,
            maintainAspectRatio: false
        }
  }),
  async mounted () {
    this.loaded = false
    try {
    //   const { userlist } = await fetch('/api/userlist')
    //   this.chartdata = userlist
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
</script>
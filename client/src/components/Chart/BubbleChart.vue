<template>
  <div>
      <canvas id="chart_bubble" width="400" height="400"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)
export default {
    name:'BubbleChart',
    props: {
        cbvalue: Number
    },

    data: () => ({
        chartdata: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
            'August', 'September', 'October', 'November', 'December'], 
            datasets:[{
                label: 'Data One',
                backgroundColor: '#f87979',
                pointBackgroundColor: 'white',
                borderWidth: 1,
                pointBorderColor: 'red',
                data:[{x: 100, y: 0, r: 10},{x: 60, y: 30, r: 20},{x: 40, y: 60, r: 25},{x: 80, y: 80, r: 50},]
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
        },
    }),
    methods: {
        fillData() {
            const ctx = document.getElementById('chart_bubble').getContext('2d')
            this.myChart = new Chart(ctx, {
                type: 'bubble',
                data: this.chartdata,
                options:this.options
                
            })
        },
        addData() {
            this.myChart.data.datasets[0].data = this.myChart.data.datasets[0].data.concat([this.cbvalue])
            this.myChart.data.labels= this.myChart.data.labels.concat(['sample'])
            
            this.myChart.update()
        }
    },
    mounted() {
        this.fillData()
    },
    watch: {
        'cbvalue': 'addData'
    }

}
</script>

<style>

</style>
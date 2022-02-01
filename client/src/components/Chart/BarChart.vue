<template>
  <div>
      <canvas id="chart" width="400" height="400"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables)
export default {
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
                data: [90, 10, 20, 30, 50, 10, 30, 40, 60, 100, 20 , 40]
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
            const ctx = document.getElementById('chart').getContext('2d')
            this.myChart = new Chart(ctx, {
                type: 'bar',
                data: this.chartdata,
                options:this.options
                
            })
        },
        addData() {
            // this.myChart.data.datasets[0].data = this.cbvalue
            // this.myChart.update()
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
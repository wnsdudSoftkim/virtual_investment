<template>
  <div>
      <canvas id="chart_bar" class="chart" ></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
import { useStore } from 'vuex'
Chart.register(...registerables)
export default {
    name:'BarChart',
    props: {
        cbvalue: Number
    },

    data: () => ({
        store: useStore(),
        chartdata: {
            datasets:[{
                label: 'Volume',
                backgroundColor: '#f87979',
                pointBackgroundColor: 'white',
                borderWidth: 1,
                pointBorderColor: 'red',
                data: []
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
                    // gridLines: {
                    //     display: false
                    // }
                }],

            },
            aspectRatio: 1,
            responsive: true,
            maintainAspectRatio: false
        },
    }),
    methods: {
        fillData() {
            const ctx = document.getElementById('chart_bar').getContext('2d')
            this.myChart = new Chart(ctx, {
                type: 'bar',
                data: this.chartdata,
                options:this.options
                
            })
        },
        addData() {
            let date = this.store.getters.updatelastdate
            console.log(date)
            this.myChart.data.datasets[0].data = this.myChart.data.datasets[0].data.concat([this.cbvalue])
            this.myChart.data.labels= this.myChart.data.labels.concat([date.substring(11,)])
            
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
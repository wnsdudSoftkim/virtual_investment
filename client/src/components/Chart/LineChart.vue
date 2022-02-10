<template>
  <div>
      <canvas id="chart_line" class="chart"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js'
import { useStore } from 'vuex'
Chart.register(...registerables)
export default {
    name:'LineChart',
    props: {
        cbvalue: Number
    },

    data: () => ({
        store: useStore(),
        chartdata: {
            datasets:[{
                label: 'Trade',
                backgroundColor: '#f87979',
                pointBackgroundColor: 'red',
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
                    gridLines: {
                        display: false
                    }
                }],

            },
            // legend: {
            //     display:true
            // },
            responsive: true,
            maintainAspectRatio: false
        },
    }),
    methods: {
        fillData() {
            const ctx = document.getElementById('chart_line').getContext('2d')
            this.myChart = new Chart(ctx, {
                type: 'line',
                data: this.chartdata,
                options:this.options
                
            })
        },
        addData() {
            let date = this.store.getters.updatelastdate
            this.myChart.data.datasets[0].data = this.myChart.data.datasets[0].data.concat([this.cbvalue])
            this.myChart.data.labels= this.myChart.data.labels.concat([date.substring(11,)])
            
            this.myChart.update()
        }
    },
    mounted() {
        this.fillData()
    },
    watch: {
        // cbvalue: function() {
        //     console.log(this.cbvalue)
            
        // }
        'cbvalue': 'addData'
    }

}
</script>

<style>

</style>
<template>
  <div>
      <canvas id="chart_bubble"  class="chart"></canvas>
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
        title: 'Income, Test Scores, and Enrollment in Select Connecticut School Districts, 2009-13',
        point_x: 'income',
        point_x_prefix: '$',
        point_x_postfix: '',
        point_y: 'grades',
        point_y_prefix:'',
        point_y_postfix:'',
        point_r:'enrollment',
        point_r_description:'Enrollment',
        point_r_prefix: '',
        point_r_postfix: '',
        r_denominator: 800,
        point_name: 'district',
        point_color: 'rgba(0, 0, 255, 0.7)',
        x_axis: 'Median Household Income, USD',
        y_axis: 'Grade, Relative to Average',
        show_grid: true,
        
    
    }),
    methods: {
        fillData() {
            const ctx = document.getElementById('chart_bubble').getContext('2d')
            const chartdata = {
                datasets:[{
                    backgroundColor: this.point_color,
                    data:[{x: 100, y: 0, r: 10},{x: 60, y: 30, r: 20},{x: 40, y: 60, r: 25},{x: 80, y: 80, r: 10}]
                }]
            }
            const options= {
                title: {
                    display: true,
                    text: this.title,
                    fontSize: 14,
                },
                legend: {
                    display: false,
                },
                scales: {
                    yAxes: [{
                        ticks:{
                           callback: function(value, index, values) { // eslint-disable-line no-unused-vars
                                return this.point_y_prefix + value.toLocaleString() + this.point_y_postfix;
                            }
                        },
                        scaleLabel: {
                            display: true,
                            labelString: this.y_axis
                        },
                        gridLines: {
                            display: this.show_grid
                        },
                    }],
                    xAxes: [{
                        scaleLable: {
                            display: true,
                            labelString: this.x_axis
                        },
                        gridLines: {
                            display: this.show_grid
                        },
                        ticks: {
                            callback: function(value, index, values) { // eslint-disable-line no-unused-vars
                                return this.point_x_prefix + value.toLocaleString() + this.point_x_postfix
                            }
                        }
                    }]

                },
                tooltips: {
                    displayColors: false,
                    callbacks: {
                        title: function(tooltipItem, all) {
                            return [
                                all.datasets[tooltipItem[0].datasetIndex].data[tooltipItem[0].index].name,
                            ]
                        },
                        label: function(tooltipItem, all) {
                            var r = all.datasets[tooltipItem.datasetIndex].data[tooltipItem.index].r * this.r_denominator;
                            return [
                                this.x_axis + ': ' + this.point_x_prefix + tooltipItem.xLabel.toLocaleString() + this.point_x_postfix,
                                this.y_axis + ': ' + this.point_y_prefix + tooltipItem.yLabel.toLocaleString() + this.point_y_postfix,
                                this.point_r_description + ': ' + this.point_r_prefix + r.toLocaleString() + this.point_r_postfix
                            ]
                        }
                    }
                },
                aspectRatio: 1,
                responsive: true,
                maintainAspectRatio: false
            }
            this.myChart = new Chart(ctx, {
                type: 'bubble',
                data: chartdata,
                options:options
                
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
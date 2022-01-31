<script>
import {Line} from 'vue3-chart-v2'
export default {

    extends: Line,
    props: {
        chartdata : {
            type: Object,
            default: null
        }
    },
    data: () => ({
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
    mounted () {
        this.renderChart(this.chartdata, this.options)
    }
}
</script>

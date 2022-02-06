<script>
import {Bar, mixins} from 'vue3-chart-v2'
const {reactiveProp} = mixins
export default {
    extends: Bar,
    mixins: [reactiveProp],
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
        this.renderChart(this.chartData, this.options)
    }
}
</script>

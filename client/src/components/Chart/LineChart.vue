<script>
import {Line} from 'vue3-chart-v2'
export default {
    extends: Line,
    data: () => ({
        datacollection: {
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
    mounted () {
        this.renderChart(this.datacollection, this.options)
    }
}
</script>

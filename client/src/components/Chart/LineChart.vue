<script>
import {Line} from 'vue3-chart-v2'
export default {
    extends: Line,
    props: {
        chartdata: {
            type: Object,
            default: null
        },
        options: {
            type: Object,
            default: null
        }
    },
    mounted () {
        this.renderChart(this.chartdata, this.options)
    }
}
</script>

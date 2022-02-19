<template>
    <div class="columns">
        <div class="button-layout">
            <div class="information">
                <reset-button></reset-button>
                <span class="info firstasset">투자금액: <b>{{this.Invest_Asset}}</b> </span>
                <span class="info nowAsset">현재금액: <b>{{this.PROPS.nowAsset}} 원</b> </span>
                <span class="info profitRate">수익률: <b>{{this.PROPS.profitRate}} %</b></span>
                <span class="info quentity">보유량: <b>{{this.quantity}}</b></span>
                <div class="footer-button">
                    <sell-button v-bind:PROPS="this.PROPS.symbol" ></sell-button>
                    <purchase-button v-bind:PROPS="this.PROPS.symbol" ></purchase-button>
                </div>
            </div>
        </div>
        <div class="column" v-if="this.headervalue == 2 || this.headervalue === 1" >
            <h3>Price</h3>
            <progressive-chart-container></progressive-chart-container>
            <description-container></description-container>
        </div>
        <div class="column" v-if="this.headervalue == 3 || this.headervalue === 1">
            <h3>Trades</h3>
            <line-chart-container></line-chart-container>
            <description-container></description-container>
        </div>
        <div class="column" v-if="this.headervalue == 4 || this.headervalue === 1" >
            <h3>Volume</h3>
            <bar-chart-container></bar-chart-container>
            <description-container></description-container>
        </div>
    </div>
</template>

<script>
import {computed} from 'vue'
import { useStore } from 'vuex'
import ResetButton from '@/components/common/button/ResetButton'
import SellButton from '@/components/common/button/SellButton'
import LineChartContainer from '@/components/ChartContainer/LineChartContainer'
import ProgressiveChartContainer from '@/components/ChartContainer/ProgressiveChartContainer'
import BarChartContainer from '@/components/ChartContainer/BarChartContainer'
import PurchaseButton from '@/components/common/button/PurchaseButton'
import DescriptionContainer from '@/components/Container/DescriptionContainer.vue'
export default {
    name:'RightSection',
    components: {ResetButton, LineChartContainer, ProgressiveChartContainer, BarChartContainer, PurchaseButton, SellButton, DescriptionContainer},
    data() {
        return {
  
            datacollection: null,
            store: useStore(),
            chart_data:null,
            server:null,
            headervalue:null,
            count:0,
            firstAsset:10000,
            nowAsset:0,
            profitRate:0,
            quantity: 0
        }
    },
    props: {
        PROPS:Object
    },
    computed: {
        check_header() {
            return this.store.getters.updateheader
        },
        Quantity() {
            return this.store.getters.getquantity
        },
        Invest_Asset() {
            return this.store.getters.getInvestAsset.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",")

        }

    },
    mounted() {
        this.headervalue = 1
        this.quantity = computed(() => this.store.getters.getquantity)
        
    },
    methods: {
        receiveProps() {
            // console.log(this.PROPS)
        }
        
    },
    watch: {
        check_header(val) {
            this.headervalue = val
        },
        'PROPS': "receiveProps"
    }
}
</script>

<style style="scss">

.button-layout {
    position:absolute;
    top:20%;
    right:8%;
    height:20rem;
    /* box-shadow: rgba(106, 36, 187, 1) */
    box-shadow: 0 4px 16px 0 rgba(0, 0, 0, .27);

}
.information {
    display: flex;
    flex-direction: column;
}
.info {
    padding:1rem;
    margin:0 auto;
    color:#000;
    font-size:18px;
}
.footer-button {
    display: flex;
}
</style>
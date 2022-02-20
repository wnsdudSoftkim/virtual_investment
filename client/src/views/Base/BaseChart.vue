<template>
    <fragment-layout >
        <!-- <div v-if="LOADING === 0" class="lottie_loading">
            <lottie-loading></lottie-loading>
        </div> -->
        <div class="main-section" >
            <left-side-bar-container ></left-side-bar-container>
            
            <right-section-container v-bind:PROPS="SEND_PROP" ></right-section-container>
        </div>
    </fragment-layout>
</template>

<script>
// import LottieLoading from '@/components/common/lottie/LottieLoading'
import FragmentLayout from '@/components/layout/FragmentLayout'
import { useStore } from 'vuex'
import {computed} from 'vue'
import methods from '@/assets/js/common.js'
import LeftSideBarContainer from '@/components/Container/LeftSideBarContainer.vue'
import RightSectionContainer from '@/components/Container/RightSectionContainer.vue'
export default {
    name:'VueChartJS',
    components: {  FragmentLayout, LeftSideBarContainer, RightSectionContainer},
    data() {
        return {
  
            datacollection: null,
            store: useStore(),
            chart_data:null,
            server:null,
            headervalue:null,
            count:0,
            firstAsset:0,
            nowAsset:0,
            profitRate:0,
            symbol:'',
            replaceAsset:'',
            loading:0,
            hasCoin:0,
            rate:0
        }
    },
    computed: {
        Chart_Data() {
            return this.chart_data
        },
        check_header() {
            return this.store.getters.updateheader
        },
        SEND_PROP() {
            return {
                'profitRate':this.profitRate,
                'nowAsset':this.replaceAsset,
                'symbol': this.symbol
            }
        },
        LOADING() {
            return this.loading
        },
        HAS_COIN() {
            return this.store.getters.getquantity
        },
        Invest_Asset() {
            return this.store.getters.getInvestAsset
        }
    },
    mounted() {
        console.log(this.loading)
        setTimeout(()=> {
            this.loading = 1
        },1900)
        this.headervalue = 1
        this.symbol = this.$route.query.symbol
        this.connect()
    },
    methods: {
        connect() {
           
            methods.chartConnect().then((server)=> {
                server.send(JSON.stringify(this.$route.query))
                server.onmessage = ({data}) => {
                    this.server = server
                    const recv = JSON.parse(data)
                    const recv_res = recv['res']

                    const recv_other = recv['other_res']
                    this.count = recv_res.length
                    this.storePrice(recv_res)
                    this.storeDate(recv_res[this.count-1]['x'])
                    this.sendData(recv_res[(this.count)-1]['x'])
                    this.storeTrade(recv_other['trades'])
                    this.storeVolume(recv_other['Volume'])

                    this.nowAsset = recv_other['Open']
                    this.storePriceAsset(this.nowAsset)
                    if (this.HAS_COIN === 0) {
                        this.profitRate = 0
                    }else {
                        this.profitRate = ((((this.HAS_COIN * this.nowAsset) / (this.Invest_Asset)) * 100)-100).toFixed(2)
                        this.store.dispatch('UpdateRate',Math.round((this.HAS_COIN * this.nowAsset)-(this.Invest_Asset)))
                    }
                    this.replaceAsset = this.nowAsset.toString().replace(/\B(?<!\.\d*)(?=(\d{3})+(?!\d))/g, ",")
                    
                    this.storeprofitRate(this.profitRate)
                }
            }).catch(err=> {
                console.log(err)
            })
        
        },
        calculateProfit(asset) {
            return ((1 + this.profitRate) * (((asset-this.Profit_Asset)/this.Profit_Asset) * 100).toFixed(2)) - 1
        },
        sendData(message) { // receive from store value
            methods.sendMessage(message)
        },
        sendTempData(message) {
            methods.sendTempMessage(message)
        },
        storePriceAsset(item) {
            this.store.dispatch('UpdatePriceAsset', item)
        },
        storeInvestAsset(item) {
            this.store.dispatch('IncreaseAsset', item)
        },
        storeTrade(item) {
            this.store.dispatch('updateTrade', item)
        },
        storeVolume(item) {
            this.store.dispatch('updateVolume', item)
        },
        storePrice(item) {
            // this.store.dispatch('updateValue', item)
            this.store.dispatch('updatePrice', item)
        },
        storeDate(item) {
            this.store.dispatch('updateLastDate', item)
        },
        storeprofitRate(item) {
            this.store.dispatch('updateProfitRate', item)
        },
        getData() {
            this.chart_data = computed(() => this.store.getters.updatechart)
        },
        disconnect() {
            methods.chartDisconnect()
        }
        
    },
    beforeRouteLeave(to, from, next) { 
        this.disconnect()
        next() 
    },

}
</script>

<style lang="scss">
li {
    display: inline-block;
    margin: 0 1rem;
}
a {
    color:$baseColor;
}
.main-section {
    display:flex;
}
.lottie_loading {
    position: absolute;
    top:30%;
    left:30%;
    z-index: 9999;
}
// canvas {
//     width:50rem;
//     height: 50rem;
// }
#chart {
    width:100%;
}
</style>
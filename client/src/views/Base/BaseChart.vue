<template>
    <fragment-layout >
        <div class="main-section">
            <left-side-bar-container></left-side-bar-container>
            <!-- title 정보와 수익률 정보를 left, 시작금액, 현재금액, 수익률 정보를 right로 보내기-->
            
            <right-section-container></right-section-container>
            <!-- <div class="button-layout">
                <reset-button>aa</reset-button>
                <div>시작금액: {{this.firstAsset}} 현재금액: {{this.nowAsset}} 수익률: {{this.profitRate}}%</div>
            </div> -->
        </div>
    </fragment-layout>
</template>

<script>
// import ResetButton from '@/components/common/button/ResetButton'
import FragmentLayout from '@/components/layout/FragmentLayout'
import { useStore } from 'vuex'
import {computed} from 'vue'
import methods from '@/assets/js/common.js'
import LeftSideBarContainer from '@/components/Container/LeftSideBarContainer.vue'
import RightSectionContainer from '@/components/Container/RightSectionContainer.vue'
export default {
    name:'VueChartJS',
    components: {  FragmentLayout, LeftSideBarContainer,RightSectionContainer },
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
            profitRate:0
        }
    },
    computed: {
        Chart_Data() {
            return this.chart_data
        },
        check_header() {
            return this.store.getters.updateheader
        }
    },
    mounted() {
        this.headervalue = 1
        this.connect()
        console.log('mount:', this.Chart_Data)
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
                    this.profitRate = (((this.nowAsset-this.firstAsset)/this.firstAsset) * 100).toFixed(2)
                    this.storeprofitRate(this.profitRate)
                }
            }).catch(err=> {
                console.log(err)
            })
        
        },
        sendData(message) { // receive from store value
            methods.sendMessage(message)
        },
        sendTempData(message) {
            methods.sendTempMessage(message)
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
            console.log(this.server)
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
</style>
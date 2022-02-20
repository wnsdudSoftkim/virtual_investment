<template>
    <div class="description-container" v-if="this.headervalue !== 1">
        <description-layout v-if="this.headervalue === 2"><p class="description_slot">{{this.template_price}}</p></description-layout>
        <description-layout v-if="this.headervalue === 3"><p class="description_slot">{{this.template_trades}}</p></description-layout>
        <description-layout v-if="this.headervalue === 4"><p class="description_slot">{{this.template_volume}}</p></description-layout>
    </div>
</template>

<script>
import {computed} from 'vue'
import DescriptionLayout from '@/components/layout/DescriptionLayout.vue'
import { useStore } from 'vuex'
export default {
    components: { DescriptionLayout },
    name: 'DescriptionContainer',
    data() {
        return {
            headervalue:1,
            store:useStore(),
            template_price: '가격에 대한 데이터이다.코인의 여러가진 요건들과 코인의 가격 정보가 포함되어 있다. 코인의 가격에 영향을 미치는 요소를 분석하고자 하는 목적으로 사용될 수 있다. 회귀분석 등의 분석에 활용될 수 있다.',
            template_trades: '거래량에 대한 데이터이다. 실제 세력들의 매집 패턴을 거래량을 통해 알 수 있다',
            template_volume: 'Volume에 대한 데이터이다. 관련 - https://marupong.tistory.com/entry/EmperorBTC-TRADING-MANUAL-%ED%95%9C%EA%B8%80-%EB%B2%88%EC%97%AD-09-%EB%B3%BC%EB%A5%A8-%EA%B1%B0%EB%9E%98%EB%9F%89%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC'
        }
    },
    mounted() {
        this.headervalue = computed(() => this.store.getters.updateheader)
    }

}
</script>

<style lang="scss">
.description-container {
    display:flex;
    justify-content: center;
    align-items:center;
}
</style>
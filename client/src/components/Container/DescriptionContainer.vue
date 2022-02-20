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
            template_volume: '거래량은 일정 기간 동안, 종종 하루 중 거래가 변경되는 자산 양입니다.거래량과 시간 경과에 따른 거래량의 변화는 기술 거래자에게 중요한 정보입니다.'
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
    margin-top:3rem;
}
</style>
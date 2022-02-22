<template>
    <div class="section-layout" >
        <div class="section-container">
            <chart-section></chart-section>
            <basic-modal></basic-modal>

        </div>
    </div>
</template>

<script>
import ChartSection from '@/components/layout/ChartSectionLayout.vue'
import BasicModal from '@/components/common/modal/BasicModal'
export default {
    name:"section-layout",
    components: {ChartSection, BasicModal},

}
</script>

<style lang="scss">
.section-layout{
    @media screen and (max-width: 768px) { 
        padding-left:0rem;
        padding-right: 0rem;
    }
    padding:2rem;
    padding-left:12rem;
    padding-right:12rem;
    .section-container{
        width:100%;
        height:40rem;
        display:flex;
        flex-direction: column;
    }
}
</style>
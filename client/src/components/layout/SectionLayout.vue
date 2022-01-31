<template>
    <div class="section-layout" >
        <div class="section-container">
            <chart-section></chart-section>
        </div>
    </div>
</template>

<script>
import ChartSection from '@/components/layout/Chart/ChartSectionLayout.vue'
export default {
    name:"section-layout",
    components: {ChartSection}

}
</script>

<style lang="scss">
.section-layout{
    padding:2rem;
    padding-left:12rem;
    padding-right:12rem;
    .section-container{
        width:100%;
        height:40rem;
        background: $secondColor;
    }
}
</style>
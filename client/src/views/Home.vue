<template>
    <div>
        <base-layout>
            <div class="section-header">
                <p class="headerText">
                  Virtual Investment with Python
                </p>
                <div class="header-section">
                    <p class="headerSubText">
                        Xangle
                    </p>
                    <p class="headerSubText">
                        Back-end, 김준영
                    </p>
                </div>
            </div>
            <section-layout></section-layout>
        </base-layout>
    </div>
</template>

<script>
import BaseLayout from '@/components/layout/BaseLayout.vue'
import SectionLayout from '../components/layout/SectionLayout.vue'
export default {
    name: 'home',
    components: { BaseLayout, SectionLayout},

}
</script>

<style lang='scss'>
.section-header{
    padding:3rem;
    border-bottom: 1px solid #eee;
    display:flex;
    flex-direction: column;
    justify-content: center;
    .header-section{
        display: flex;
        justify-content: space-around;
    }
}
</style>
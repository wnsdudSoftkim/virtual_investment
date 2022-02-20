<template>
    <div class="rightSectionContainer">
        <right-section v-bind:PROPS="this.PROPS">
        </right-section>
    </div>
</template>

<script>
import RightSection from '@/components/layout/RightSection.vue'

export default {
    name:'RightSectionContainer',
    components: {RightSection},
    props: {
        PROPS:Object
    },

}
</script>

<style>
.rightSectionContainer {
    width:100%;
}

</style>
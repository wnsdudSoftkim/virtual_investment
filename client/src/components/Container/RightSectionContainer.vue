<template>
    <div class="rightSectionContainer">
        <right-section>
        </right-section>
    </div>
</template>

<script>
import RightSection from '@/components/layout/RightSection.vue'

export default {
    name:'RightSectionContainer',
    components: {RightSection}
}
</script>

<style>
.rightSectionContainer {
    width:100%;
}

</style>
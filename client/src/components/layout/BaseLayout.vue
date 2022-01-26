<template>
    <div class="base-layout">
        <slot></slot>
        <main-footer></main-footer>
    </div>
</template>

<script>
import MainFooter from '@/components/Footer'
export default {
    name:'base-layout',
    components: {MainFooter}
}
</script>

<style lang="scss">
@import "@/assets/scss/_base";
.base-layout{
    height:100%;
}

</style>
<template>
    <div class="base-layout">
        <slot></slot>
        <footer-container></footer-container>
    </div>
</template>

<script>
import FooterContainer from '@/components/Container/FooterContainer'
export default {
    name:'base-layout',
    components: {FooterContainer}
}
</script>

<style lang="scss">
@import "@/assets/scss/_base";
.base-layout{
    height:100%;
}

</style>
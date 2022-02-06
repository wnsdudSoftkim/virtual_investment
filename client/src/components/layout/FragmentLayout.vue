<template>
   <div class="fragment-layout">
        <fragment-header></fragment-header>
        <slot></slot>
    </div>
</template>

<script>
import FragmentHeader from '@/components/FragmentHeader'
export default {
    components: {FragmentHeader}
}
</script>

<style lang="scss">
    .fragment-layout{
        height:100%;
    }

</style>
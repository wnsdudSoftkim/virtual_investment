<template>
    <div class="base-layout">
        <div class="section">

        </div>
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

<style>
.base-layout{
    height:100%;
    min-height: 700px;
}

</style>
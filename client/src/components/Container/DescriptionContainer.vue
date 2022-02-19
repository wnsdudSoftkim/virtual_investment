<template>
    <div class="description-container" v-if="this.headervalue !== 1">
        <description-layout>asdasd{{this.headervalue}}</description-layout>
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
            store:useStore()
        }
    },
    mounted() {
        this.headervalue = computed(() => this.store.getters.updateheader)
        console.log(this.headervalue)
    }

}
</script>

<style>

</style>
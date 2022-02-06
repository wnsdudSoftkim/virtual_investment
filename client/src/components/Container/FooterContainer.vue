<template>
    <div>
        <main-footer v-bind:cbvalue="cbvalue"></main-footer>
    </div>
</template>

<script>
import MainFooter from '@/components/layout/Footer'
import { useStore } from 'vuex'
import {computed} from 'vue'
export default {
    name:'FooterContainer',
    components: { MainFooter},
    data: ()=> ({
        cbvalue:0,
        store:useStore()
    }),
    mounted() {
        this.profitFooter()
    },
    methods: {
        profitFooter() {
            this.cbvalue= computed(() => this.store.getters.updateprofitrate)
        }
    }
}
</script>

<style>

</style>
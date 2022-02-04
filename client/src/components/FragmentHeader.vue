<template>
    <div class="fragment-header">
        <green-button>
             <router-link to='/'>Home</router-link>
        </green-button>
        <green-button @click='onClick(1)'>
            base
        </green-button>
        <green-button @click='onClick(2)'>
            progressvie
        </green-button>
        <green-button @click='onClick(3)'>
            line
        </green-button>
        <green-button @click='onClick(4)'>
            bubble
        </green-button>
        <green-button @click='onClick(5)'>
           bar
        </green-button>
    </div>
  
</template>

<script>
import GreenButton from '@/components/common/button/GreenButton'
import { useStore } from 'vuex'
export default {
    name:'fragment-header',
    components: {GreenButton},
    data() {
        return {
            store:useStore()
        }
    },
    methods: {
        onClick(value) {
            this.store.dispatch('updateHeader', value)
        }
    },
}
</script>

<style lang="scss">
.fragment-header {
    display:flex;
    justify-content: space-around;
}
</style>
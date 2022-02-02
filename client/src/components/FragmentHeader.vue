<template>
    <div class="fragment-header">
        <green-button>
             <router-link to='/'>Home</router-link>
        </green-button>
        <green-button>
            <router-link to='/chart/#progressvie'>progressvie</router-link>
        </green-button>
        <green-button>
            <router-link to='/chart/#line'>line</router-link>
        </green-button>
        <green-button>
           <router-link to='/chart/#bar'>bar</router-link>
        </green-button>
    </div>
  
</template>

<script>
import GreenButton from '@/components/common/button/GreenButton'
export default {
    name:'fragment-header',
    component: {GreenButton}
}
</script>

<style lang="scss">
.fragment-header {
    display:flex;
    justify-content: space-around;
}
</style>
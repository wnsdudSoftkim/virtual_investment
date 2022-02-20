<template>
    <div class="fragment-header">
        <!-- <green-button @click='onClick(1)'>
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
        </green-button> -->
        <ul class="horizontal">
            <li>
                <a class="active" @click="onClick(1)">Base</a>
                <div style="background:#04AA6D;; height:3px;" v-if="this.header === 1" >--</div>
            </li>
            <li>
                <a  @click="onClick(2)">Price</a>
                    <div style="background:#04AA6D;; height:3px;" v-if="this.header === 2" >--</div>
            </li>
            <li>
                <a  @click="onClick(3)">Trade</a>
                    <div style="background:#04AA6D;; height:3px;" v-if="this.header === 3" >--</div>
            </li>
            <li>
                <a  @click="onClick(4)">Volume</a>
                    <div style="background:#04AA6D;; height:3px;" v-if="this.header === 4" >--</div>
            </li>
        </ul>
    </div>
  
</template>

<script>
// import GreenButton from '@/components/common/button/GreenButton'
import { useStore } from 'vuex'
export default {
    name:'fragment-header',
    // components: {GreenButton},
    data() {
        return {
            store:useStore(),
            header:1
        }
    },
    methods: {
        onClick(value) {
            this.header = value
            this.store.dispatch('updateHeader', value)
        }
    },
}
</script>

<style lang="scss">
.horizontal {
    list-style-type: none;
    margin:0;
    padding:0;
    overflow:hidden;
    background-color: $baseColor;
    display: flex;
    justify-content: space-around;
    a{
        align-content: center;
        display: inline-block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        font-size: 18px;
        text-decoration: none;
        cursor: pointer;
        &:hover {
            background-color: $secondColor;
        }

    }
}
</style>
<template>
    <button class="button-64" role="button" @click="changeButtonValue"><span class="text">{{this.button_value}}</span></button>
  
</template>

<script>
import methods from '@/assets/js/common.js'
import {useStore} from 'vuex'
export default {
    
    name:'ResetButton',
    data: ()=> ({
        button_flag: false,
        button_value: "STOP",
        store: useStore()
    }),
    methods: {
        changeButtonValue() {
            let message = this.store.getters.updatelastdate
            console.log(message)
            this.button_value = this.button_flag ? "STOP" : "START"
            this.button_flag = !this.button_flag
            console.log(message)
            console.log(this.button_flag)
            if (this.button_flag === true) {
              methods.sendMessage(1)
            }else {
              methods.sendMessage(message)
            }
           
           
        }
    } 
}
</script>

<style lang="scss">
.button-64 {
  align-items: center;
  border: 0;
  border-radius: 8px;
  box-sizing: border-box;
  color: #000;
  display: flex;
  font-family: Phantomsans, sans-serif;
  font-size: 20px;
  justify-content: center;
  line-height: 1em;
  max-width: 100%;
  min-width: 140px;
  padding: 3px;
  text-decoration: none;
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  white-space: nowrap;
  cursor: pointer;
}

.button-64:active,
.button-64:hover {
  outline: 0;

}

.button-64 span {
  background-color: white;
  padding: 16px 24px;
  border-radius: 6px;
  width: 100%;
  height: 100%;
  transition: 300ms;
}



@media (min-width: 768px) {
  .button-64 {
    font-size: 24px;
    min-width: 196px;
  }
}
</style>